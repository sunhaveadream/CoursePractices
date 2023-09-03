from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Topic, Entry,Teacher,TeacherMessage
from .forms import TopicForm, EntryForm,TeacherForm,TeacherMessageForm

def index(request):
    """The home page for Learning Log."""
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    """Show all topics."""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = Topic.objects.get(id=topic_id)
    # Make sure the topic belongs to the current user.
    if topic.owner != request.user:
        raise Http404

    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    """Add a new topic."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs:topics')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    topic = Topic.objects.get(id=topic_id)
    
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EntryForm()
    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)

    # Display a blank or invalid form.
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404
    
    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)


@login_required
def teachers(request):
    """Show all teachers."""
    teachers = Teacher.objects.filter(owner=request.user).order_by('date_added')
    context = {'teachers': teachers}
    return render(request, 'learning_logs/teachers.html', context)


@login_required
def teacher(request, teacher_id):
    """Show a single teacher and all its teacherMessages."""
    teacher = Teacher.objects.get(id=teacher_id)
    # Make sure the teacher belongs to the current user.
    if teacher.owner != request.user:
        raise Http404

    teacherMessages = teacher.teachermessage_set.order_by('-date_added')
    context = {'teacher': teacher, 'teacherMessages': teacherMessages}
    return render(request, 'learning_logs/teacher.html', context)


@login_required
def new_teacher(request):
    """Add a new teacher."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TeacherForm()
    else:
        # POST data submitted; process data.
        form = TeacherForm(data=request.POST)
        if form.is_valid():
            new_teacher = form.save(commit=False)
            new_teacher.owner = request.user
            new_teacher.save()
            return redirect('learning_logs:teachers')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'learning_logs/new_teacher.html', context)


@login_required
def new_teacherMessage(request, teacher_id):
    """Add a new teacherMessage for a particular teacher."""
    teacher = Teacher.objects.get(id=teacher_id)

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TeacherMessageForm()
    else:
        # POST data submitted; process data.
        form = TeacherMessageForm(data=request.POST)
        if form.is_valid():
            new_teacherMessage = form.save(commit=False)
            new_teacherMessage.teacher = teacher
            new_teacherMessage.save()
            return redirect('learning_logs:teacher', teacher_id=teacher_id)

    # Display a blank or invalid form.
    context = {'teacher': teacher, 'form': form}
    return render(request, 'learning_logs/new_teacherMessage.html', context)


@login_required
def edit_teacherMessage(request, teacherMessage_id):
    """Edit an existing teacherMessage."""
    teacherMessage = TeacherMessage.objects.get(id=teacherMessage_id)
    teacher = teacherMessage.teacher
    if teacher.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Initial request; pre-fill form with the current teacherMessage.
        form = TeacherMessageForm(instance=teacherMessage)
    else:
        # POST data submitted; process data.
        form = TeacherMessageForm(instance=teacherMessage, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:teacher', teacher_id=teacher.id)
    context = {'teacherMessage': teacherMessage, 'teacher': teacher, 'form': form}
    return render(request, 'learning_logs/edit_teacherMessage.html', context)


@login_required
def delete_teacherMessage(request, teacherMessage_id):
    """Delete an existing teacherMessage."""
    teacherMessage = TeacherMessage.objects.get(id=teacherMessage_id)
    teacher = teacherMessage.teacher
    if teacher.owner != request.user:
        raise Http404

    if request.method == 'POST':
        # POST data submitted; delete the teacherMessage.
        teacherMessage.delete()
        return redirect('learning_logs:teacher', teacher_id=teacher.id)

    context = {'teacherMessage': teacherMessage, 'teacher': teacher}
    return render(request, 'learning_logs/delete_teacherMessage.html', context)
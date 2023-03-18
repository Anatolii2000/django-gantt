from django.shortcuts import render
import json

def main_menu(request):

    tasks = [
    {
        "id": 'Task 1',
        "name": 'AIPLAT',
        "start": '2022-01-22',
        "end": '2022-01-23',
        "progress": 20,
        #"custom_class": 'cc-red',
    },
    {
        "id" :'Task 2',
        "name": 'BIROOT',
        "start": '2022-01-23',
        "end": '2022-01-25',
        "progress": 5,
        "custom_class": 'cc-red',
    },
    {
        "id": 'Task 3',
        "name": 'KDL',
        "start": '2022-01-25',
        "end": '2022-01-27',
        "progress": 10,
        "dependencies": 'Task 2',
        "custom_class": 'bar-maintask'
    },
    {
        "id": 'Task 4',
        "name": 'MIRROR',
        "start": '2022-02-01',
        "end": '2022-02-03',
        "progress": 58,
        "dependencies": 'Task 3',
        "custom_class": 'cc-red',
    },
    {
        "id": 'Task 5',
        "name": 'OUV',
        "start": '2022-02-03',
        "end": '2022-02-07',
        "progress": 90,
        "custom_class": 'bar-maintask'
    },
    {
        "id": 'Task 6',
        "name": 'QA',
        "start": '2022-02-07',
        "end": '2022-02-09',
        "progress": 50,
        "dependencies": 'Task 4, Task 5, Task 1'
    },
    {
        "id": 'Task 6',
        "name": 'IUSRTK',
        "start": '2022-02-07',
        "end": '2022-02-09',
        "progress": 50,
        "dependencies": 'Task 4, Task 5, Task 1'
    }

    ]
    # form = BaseGantt()
    # form.set_time_scale("Day")
    params = {
            "title":"Тест диаграммы Гантт",
            "gantt":tasks,
            "read_only":False,
            }
    info = { 'info': params}
    with open('my_test_django/static/gantt.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(tasks, ensure_ascii=False))
    print(json.dumps(tasks))

    return render(request,"index.html")

def heroes(request):
    return render(request, "heroes.html")

def gantt(request):
    return render(request, "gantt.html")

def main(request):
    return render(request, "main.html")
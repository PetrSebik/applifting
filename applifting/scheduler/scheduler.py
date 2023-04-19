from django.utils import timezone
from django_q.models import Schedule


def schedule_tasks():
    """
    function to list all the scheduled tasks that are run by the django-q module
    only one schedule per called function by the scheduler (first argument) - this is to avoid duplicated in DB
    keep in mind that the cron times are in UTC
    """
    schedule('applifting.offer.schedules.update_offers', schedule_type=Schedule.CRON, cron='*/1 * * * *')


def schedule(func, *args, **kwargs) -> Schedule:
    """
    get or create a schedule
    custom function based on django_q.schedule function

    :param func: function to schedule.
    :param args: function arguments.
    :param name: optional name for the schedule.
    :param hook: optional result hook function.
    :type schedule_type: Schedule.TYPE
    :param repeats: how many times to repeat. 0=never, -1=always.
    :param next_run: Next scheduled run.
    :type next_run: datetime.datetime
    :param cluster: optional cluster name.
    :param cron: optional cron expression
    :param kwargs: function keyword arguments.
    :return: the schedule object.
    :rtype: Schedule
    """

    name = kwargs.pop("name", None)
    hook = kwargs.pop("hook", None)
    schedule_type = kwargs.pop("schedule_type", Schedule.ONCE)
    minutes = kwargs.pop("minutes", None)
    repeats = kwargs.pop("repeats", -1)
    next_run = kwargs.pop("next_run", timezone.now())
    cron = kwargs.pop("cron", None)
    cluster = kwargs.pop("cluster", None)

    # get or create and return the schedule
    s, created = Schedule.objects.get_or_create(func=func)
    s.name = name
    s.hook = hook
    s.args = args
    s.kwargs = kwargs
    s.schedule_type = schedule_type
    s.minutes = minutes
    s.repeats = repeats
    s.next_run = next_run
    s.cron = cron
    s.cluster = cluster

    # this is run by django command `qmigrate`, so print the status to the console
    if created:
        print(f"{func} - created")

    # validation before saving
    s.full_clean()
    s.save()
    return s


def clear_finished_schedules():
    """
    clear schedules that have 0 repeats left
    """
    Schedule.objects.filter(repeats=0).all().delete()

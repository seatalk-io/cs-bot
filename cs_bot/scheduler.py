"""
Copyright 2022 SeaTalk Open Platform

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import datetime
import traceback
from concurrent.futures import ThreadPoolExecutor
from threading import Lock
from typing import Callable, Hashable, Union

import schedule

from cs_bot import logger


class Scheduler(schedule.Scheduler):
    def __init__(self, background_workers: int = 16):
        super(Scheduler, self).__init__()
        self._lock = Lock()
        self._scheduler_thread_pool: ThreadPoolExecutor = ThreadPoolExecutor(
            max_workers=background_workers
        )

    def run_pending(self):
        if self._lock.locked():
            return
        with self._lock:
            super().run_pending()

    def every(self, interval: int = 1) -> 'Job':
        return Job(interval, self)

    @property
    def pool(self) -> ThreadPoolExecutor:
        return self._scheduler_thread_pool


class Job(schedule.Job):
    def __init__(self, interval: int, scheduler: Scheduler = None):
        super(Job, self).__init__(interval, scheduler)
        self.scheduler = scheduler
        self.once: bool = False

    def background_job_wrapper(self, f: Callable) -> Callable:
        def done_callback(worker):
            exception = worker.exception()
            if exception:
                logger.error("Scheduler Job executiong error: %s\n", exception, traceback.format_exc())

        def inner(*args, **kwargs):
            if self.once:
                self.scheduler.cancel_job(self)
            self.scheduler.pool.submit(f, *args, **kwargs).add_done_callback(done_callback)

        return inner

    def once(self, job_func: Callable, *args, **kwargs):
        self.once = True
        return super(Job, self).do(self.background_job_wrapper(job_func), *args, **kwargs)

    def do(self, job_func: Callable, *args, **kwargs):
        return super(Job, self).do(self.background_job_wrapper(job_func), *args, **kwargs)

    def block_do(self, job_func: Callable, *args, **kwargs):
        return super(Job, self).do(job_func, *args, **kwargs)

    @property
    def second(self):
        _ = super(Job, self).second
        return self.seconds

    @property
    def seconds(self):
        _ = super(Job, self).seconds
        return self

    @property
    def minute(self):
        _ = super(Job, self).minute
        return self.minutes

    @property
    def minutes(self):
        _ = super(Job, self).minutes
        return self

    @property
    def hour(self):
        _ = super(Job, self).hour
        return self.hours

    @property
    def hours(self):
        _ = super(Job, self).hours
        return self

    @property
    def day(self):
        _ = super(Job, self).day
        return self.days

    @property
    def days(self):
        _ = super(Job, self).days
        return self

    @property
    def week(self):
        _ = super(Job, self).week
        return self.weeks

    @property
    def weeks(self):
        _ = super(Job, self).weeks
        return self

    @property
    def monday(self):
        _ = super(Job, self).monday
        return self.weeks

    @property
    def tuesday(self):
        _ = super(Job, self).tuesday
        return self.weeks

    @property
    def wednesday(self):
        _ = super(Job, self).wednesday
        return self.weeks

    @property
    def thursday(self):
        _ = super(Job, self).thursday
        return self.weeks

    @property
    def friday(self):
        _ = super(Job, self).friday
        return self.weeks

    @property
    def saturday(self):
        _ = super(Job, self).saturday
        return self.weeks

    @property
    def sunday(self):
        _ = super(Job, self).sunday
        return self.weeks

    def tag(self, *tags: Hashable):
        super(Job, self).tag()
        return self

    def at(self, time_str):
        super(Job, self).at(time_str)
        return self

    def to(self, latest: int):
        super(Job, self).to(latest)
        return self

    def until(
            self,
            until_time: Union[datetime.datetime, datetime.timedelta, datetime.time, str],
    ):
        super(Job, self).until(until_time)
        return self

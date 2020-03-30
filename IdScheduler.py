import sched
import time
import datetime
# sample ids
ACCOUNT_IDS = [1000,1001,1002,1003,1004,1005, 1006, 
               1007,1008,1009,1010,1011,1012, 1013, 
               1014,1015,1016,1017,1018,1019, 1020, 
               1021,1022,1023,1024,1025,1026, 1027, 
               1028,1029,1030,1031,1032,1033, 1034,
               1035,1036,1037,1038,1039,1040, 1041]

# ACCOUNT_IDS = [1000,1001,1002, 1003]


class IdScheduler():

    ids_to_return = []
    scheduler = sched.scheduler(time.time, time.sleep)

    def _cleanSchedule(self):
        """Cleans the schedule stack of events
           to prevent time colision 
        """

        for event in self.scheduler.queue:
            self.scheduler.cancel(event)


    def _createsubsets(self, idlist):
        """Create x amount of sublists
        
        Arguments:
            idlist {[list]} -- [list of Ids]
        
        Returns:
            [list] -- [list of sublist]
        """
        subsetted_list = []
        sublist = []
        length = len(idlist)

        for index, elem in enumerate(idlist):
            if len(sublist) == 5 or length==index:
                subsetted_list.append(sublist)
                sublist = []
                sublist.append(elem)
                continue

            elif len(sublist) < 5:
                sublist.append(elem)
                
            if length==index+1:
                if elem not in sublist:
                    sublist.append(elem)
                subsetted_list.append(sublist)
        return subsetted_list


    def _runId(self, ids_set):
        """Make id available

        Arguments:
            accountId {[integer]} -- [Account Id to display]

        """
        if ids_set not in self.ids_to_return:
            self.ids_to_return.append(ids_set)


    def _getIds(self):
        """Display available Ids
           Print Ids and time of dislpay
        """
        time = datetime.datetime.now().time()
        if len(self.ids_to_return) > 0:
            print('{} {} {} {}'.format("Ids at this time:", self.ids_to_return, "Computer Clock", time))
            self.ids_to_return = []
        else:
            print("No Ids at this time: {}".format(time) )


    def _set_idsSet_schedules(self, ids_set=[],  priority=1, id_buffer=60):
        """Schedules set of ids by specified time and task priority 
        
        Keyword Arguments:
            ids_set {list} -- [list of Ids] (default: {[]})
            priority {int} -- [priority number] (default: {1})
            id_buffer {int} -- [interval after previous Id in seconds] (default: {60})
        """

        self.scheduler.enter(id_buffer, priority, self._runId,
                                argument=(ids_set,))


    def _set_display_schedule(self, interval=60):
        """[Schedules by minute to display results]
        """
        self.scheduler.enter(interval, 1, self._set_display_schedule,
                             argument=(interval,))
        self._getIds()
       

    def set_ids(self, account_ids=[], id_interval=900, res_interval=60):
        """[Entry point, sets scheduler for each id
            and schedule to return Ids with specified time]
        Arguments:
            args(
                'account_ids'(list) -- [collection of integers]
                'id_interval'(interger) -- [time in seconds to next id]
                'res_interval'(interger) -- [time in seconds to display result]
            )
        """
        if len(self.scheduler.queue) > 0:
            # if this is not first iteration, clean used events
            self._cleanSchedule()

        id_buffer = 1
        priority = 2
        subsets = self._createsubsets(account_ids)

        if subsets is not None:
            for idset in subsets:
                self._set_idsSet_schedules(ids_set=idset, priority=priority, id_buffer=id_buffer)
                id_buffer += 60
                priority += 1
            
            self._set_display_schedule(interval=res_interval)
        else:
            pass
        self.scheduler.enter(id_interval, priority, self.set_ids,
                             argument=(account_ids,
                                       id_interval,
                                       res_interval))


if __name__ == "__main__":
    idscheduler = IdScheduler()
    # Id interval of 15 min and refresh results every minute
    idscheduler.set_ids(account_ids=ACCOUNT_IDS)


    """ NOTE: If you want to Adjust Time intervals follow example below"""
    # the followng command will schedule Ids with an
    # interval of 1 min and refresh results every 30 seconds
    #
    # idscheduler.set_ids(account_ids=ACCOUNT_IDS,
    #                     id_buffer=60, res_interval=15)

    idscheduler.scheduler.run()

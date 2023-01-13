class Site:
    def __int__(self, start_time, end_time, a_num, b_num):
        self.start_time = start_time
        self.end_time = end_time
        self.charge_node = dict()
        self.is_existing = False

    def expand(self, num):
        for i in range(num):
            self.charge_node = 0
            pass
        return 1


class ExistingSite(Site):
    def __int__(self, start_time, end_time, a_num, b_num, kpi1, kpi2):
        self = Site(start_time, end_time, a_num, b_num)
        self.kpi1 = None
        self.kpi2 = None


class PlanningSite(Site):
    def __int__(self, start_time, end_time, a_num, b_num, kpi1, kpi2):
        self = Site(start_time, end_time, a_num, b_num)
        self.kpi1 = None
        self.kpi2 = None

    def expand(self, num):
        pass



if __name__ == '__main__':
    existing_
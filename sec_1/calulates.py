from datetime import datetime, timedelta
from typing import List

class Record:
    def __init__(self, amount: int, comment: str, date=datetime.now().date()):
        self._amount = amount
        self._comment = comment
        self._date = date 
    
    @property
    def amount(self):
        return self._amount
    
    @amount.setter
    def amount(self, amount):
        self._amount = amount

    @property 
    def date(self):
        return self._date
    
    def __str__(self) -> str:
        return f'{self._amount}| {self._comment}| {self._date}'
    

class Calculator:
    def __init__(self, limit: int):
        self.limit = limit
        self.records = []

    # добавить запись
    def add_record(self, *records: List[Record]):
        for record in records:
            self.records.append(record)
    
    #статистика за день
    def get_today_stats(self) -> int:
        date_now = datetime.now().date()
        sum = 0

        for record in self.records:
            if date_now == record.date:
                sum += record.amount
        return sum
    
    #статистика за неделю 
    def get_week_status(self) -> int:
        week_ago = datetime.now().date() - timedelta(weeks=1)
        sum = 0

        for record in self.records:
            if  week_ago <= record.date:
                sum += record.amount
        return sum


class CaloriesCalculator(Calculator):
    #сколько еще можно потратить
    def get_caluries_remained(self) -> str:
        cash_today = self.get_today_stats()
        status = self.limit - cash_today

        if status >= 0:
            return f'У вас осталось: {status} kal'
        return f'Вы переели: {-status} kal'


class CashCalculator(Calculator):
    #сколько еще можно съесть
    def get_today_cash_remained(self) -> str:
        cash_today = self.get_today_stats()
        status = self.limit - cash_today

        if status >= 0:
            return f'У вас осталось: {status}'
        return f'У вас Долг: {status}'


def main():
    ccalc = CaloriesCalculator(1000)
    r = Record(100, 'ccie')
    r2 = Record(520, 'self')
    ccalc.add_record(r,r2)
    ccalc.add_record(r2)

    print(ccalc.get_today_stats())
    print(ccalc.get_caluries_remained())

    calc = CashCalculator(1000)
    calc.add_record(r)
    calc.add_record(r2)
    print(calc.get_today_cash_remained())

if __name__ == '__main__':
    main()
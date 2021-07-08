"""
크롤러 1 구독옵션 (기본값 All True)
    - STOCK_VI_ON_OFF
    - KOSPI_ORDER_BOOK
    - KOSPI_TICK
    - KOSPI_AFTER_MARKET_ORDER_BOOK
    - KOSPI_AFTER_MARKET_TICK
    - STOCK_VI_ON_OFF
    - KOSPI_BROKER_INFO
    - STOCK_FUTURES_ORDER_BOOK
    - STOCK_FUTURES_TICK

크롤러 2 구독옵션 (기본값 All True)
    - KOSDAQ_ORDER_BOOK
    - KOSDAQ_TICK
    - KOSDAQ_AFTER_MARKET_ORDER_BOOK
    - KOSDAQ_AFTER_MARKET_TICK
    - KOSDAQ_BROKER_INFO
"""

from xing_tick_crawler.crawler import crawler_1, crawler_2
from datetime import datetime
from multiprocessing import Process, get_context
from multiprocessing.queues import Queue

if __name__ == "__main__":
    crawler_1_subs_option = {
        # 주식 VI 정보 off
        'STOCK_VI_ON_OFF': False,
    }
    crawler_2_subs_option = {
        
    }

    queue = Queue(ctx=get_context())
    p0 = Process(target=crawler_1, args=(queue,), kwargs=crawler_1_subs_option)
    p1 = Process(target=crawler_2, args=(queue,), kwargs=crawler_2_subs_option)

    p0.start()
    p1.start()

    while True:
        tick = queue.get()
        waiting_tasks = queue.qsize()
        tick_type, tick_data = tick
        print(f"\r{datetime.now()} waiting tasks : {'%6d' % waiting_tasks}", end='')
        print(tick_type, tick_data)

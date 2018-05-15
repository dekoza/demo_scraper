from decimal import Decimal
import feedparser
import pendulum
import logging

from sunscraper.taskapp.celery import app

from . import models

logger = logging.getLogger('celery')


@app.task(bind=True)
def scrape_currency_rsses():
    # TODO: parallelize
    for currency in models.Currency.objects.all():
        feed = feedparser.parse(currency.rss_link)
        for entry in feed.entries:
            date = pendulum.parse(entry.updated).in_tz('utc').date()
            currency_code = entry.cb_targetcurrency
            if currency_code != currency.code:
                logger.error(
                    f"Currency code mismatch parsing {feed.url}: expected {currency.code}, got {currency_code}")
                break
            rate_value = Decimal(entry.cb_exchangerate.split('\n')[0])
            models.Rate.objects.get_or_create(date=date, currency=currency, defaults={'value': rate_value})

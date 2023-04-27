from city_scrapers_core.constants import NOT_CLASSIFIED
from city_scrapers_core.items import Meeting
from city_scrapers_core.spiders import CityScrapersSpider
import json
import scrapy


class ChiMetroPlanningSpider(CityScrapersSpider):
    name = "chi_metro_planning"
    agency = "Chicago Metropolitan Agency for Planning"
    timezone = "America/Chicago"
    start_urls = ["https://www.cmap.illinois.gov/events?p_p_id=com_liferay_calendar_web_portlet_CalendarPortlet_INSTANCE_CsoLzKTepXRS&p_p_lifecycle=2&p_p_cacheability=cacheLevelPage&doAsUserId=&p_p_resource_id=calendarBookings"]
    #start_urls = ["https://www.cmap.illinois.gov/events"]

    """
    my_data={'p_p_id':'com_liferay_calendar_web_portlet_CalendarPortlet_INSTANCE_CsoLzKTepXRS', 'p_p_lifecycle': 2, 'p_p_cacheability':'cacheLevelPage', 'doAsUserId': '', 'p_p_resource_id': 'calendarBookings'}
    request = scrapy.Request("https://www.cmap.illinois.gov/events?p_p_id=com_liferay_calendar_web_portlet_CalendarPortlet_INSTANCE_CsoLzKTepXRS&p_p_lifecycle=2&p_p_cacheability=cacheLevelPage&doAsUserId=&p_p_resource_id=calendarBookings", method='POST', 
                        body=json.dumps(my_data), 
                        headers={':authority': 'www.cmap.illinois.gov', ':method': 'POST', ':path': '/events?p_p_id=com_liferay_calendar_web_portlet_CalendarPortlet_INSTANCE_CsoLzKTepXRS&p_p_lifecycle=2&p_p_cacheability=cacheLevelPage&doAsUserId=&p_p_resource_id=calendarBookings', ':scheme': 'https', 'accept': '*/*', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8', 'content-length': 1170, 'content-type': 'application/x-www-form-urlencoded;charset=UTF-8', 'cookie': 'COOKIE_SUPPORT=true; GUEST_LANGUAGE_ID=en_US; _gid=GA1.2.1261807968.1682515569; JSESSIONID=A920F6337E6233A73BD99CD4FBF28F01; _gauges_unique_hour=1; _gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1; _ga_SJFHXK8DE5=GS1.1.1682540080.5.1.1682541108.0.0.0; _ga=GA1.2.358625250.1682515565; _gat=1; LFR_SESSION_STATE_10158=1682541109677', 'origin': 'https://www.cmap.illinois.gov', 'referer': 'https://www.cmap.illinois.gov/events', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36', 'x-csrf-token': 'qsTV75DI'} )
    """

    def parse(self, response):
        """
        `parse` should always `yield` Meeting items.

        Change the `_parse_title`, `_parse_start`, etc methods to fit your scraping
        needs.
        """
        #jsonresponse = json.loads(response.text)
        #print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHAAAAAAAAAAAAAAAAAAAAAAAAAAAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH')
        #print('jsonresponse', jsonresponse)

        #print(response.body)
        """
        my_data={'p_p_id':'com_liferay_calendar_web_portlet_CalendarPortlet_INSTANCE_CsoLzKTepXRS', 'p_p_lifecycle': 2, 'p_p_cacheability':'cacheLevelPage', 'doAsUserId': '', 'p_p_resource_id': 'calendarBookings'}
        request = scrapy.Request("https://www.cmap.illinois.gov/events?p_p_id=com_liferay_calendar_web_portlet_CalendarPortlet_INSTANCE_CsoLzKTepXRS&p_p_lifecycle=2&p_p_cacheability=cacheLevelPage&doAsUserId=&p_p_resource_id=calendarBookings", method='POST', 
                          body=json.dumps(my_data), 
                          headers={':authority': 'www.cmap.illinois.gov', ':method': 'POST', ':path': '/events?p_p_id=com_liferay_calendar_web_portlet_CalendarPortlet_INSTANCE_CsoLzKTepXRS&p_p_lifecycle=2&p_p_cacheability=cacheLevelPage&doAsUserId=&p_p_resource_id=calendarBookings', ':scheme': 'https', 'accept': '*/*', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8', 'content-length': 1170, 'content-type': 'application/x-www-form-urlencoded;charset=UTF-8', 'cookie': 'COOKIE_SUPPORT=true; GUEST_LANGUAGE_ID=en_US; _gid=GA1.2.1261807968.1682515569; JSESSIONID=A920F6337E6233A73BD99CD4FBF28F01; _gauges_unique_hour=1; _gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1; _ga_SJFHXK8DE5=GS1.1.1682540080.5.1.1682541108.0.0.0; _ga=GA1.2.358625250.1682515565; _gat=1; LFR_SESSION_STATE_10158=1682541109677', 'origin': 'https://www.cmap.illinois.gov', 'referer': 'https://www.cmap.illinois.gov/events', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36', 'x-csrf-token': 'qsTV75DI'} )
        """
        #print(response.json())
        print(response.body)

        
        """try:
            data = json.loads(response.body)
            print(data[0]["title"])
        except json.JSONDecodeError as e:
            print(e)"""
        
        """data = json.loads(response.body)
        for elem in data:
            print(elem["title"])"""
        
        """if response:
            data = json.loads(response.body)
            print(data)
        else:
            print("why")"""

        for item in response.css(".meetings"):
            meeting = Meeting(
                title=self._parse_title(item),
                description=self._parse_description(item),
                classification=self._parse_classification(item),
                start=self._parse_start(item),
                end=self._parse_end(item),
                all_day=self._parse_all_day(item),
                time_notes=self._parse_time_notes(item),
                location=self._parse_location(item),
                links=self._parse_links(item),
                source=self._parse_source(response),
            )

            meeting["status"] = self._get_status(meeting)
            meeting["id"] = self._get_id(meeting)

            yield meeting

    def _parse_title(self, item):
        """Parse or generate meeting title."""
        return ""

    def _parse_description(self, item):
        """Parse or generate meeting description."""
        return ""

    def _parse_classification(self, item):
        """Parse or generate classification from allowed options."""
        return NOT_CLASSIFIED

    def _parse_start(self, item):
        """Parse start datetime as a naive datetime object."""
        return None

    def _parse_end(self, item):
        """Parse end datetime as a naive datetime object. Added by pipeline if None"""
        return None

    def _parse_time_notes(self, item):
        """Parse any additional notes on the timing of the meeting"""
        return ""

    def _parse_all_day(self, item):
        """Parse or generate all-day status. Defaults to False."""
        return False

    def _parse_location(self, item):
        """Parse or generate location."""
        return {
            "address": "",
            "name": "",
        }

    def _parse_links(self, item):
        """Parse or generate links."""
        return [{"href": "", "title": ""}]

    def _parse_source(self, response):
        """Parse or generate source."""
        return response.url
    

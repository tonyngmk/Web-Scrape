import scrapy
import datetime
import json

class MyItem(scrapy.Item):
    # Date = scrapy.Field()
    EXT_Course_Ref_No = scrapy.Field()
    Course_Title = scrapy.Field()
    Course_Objective = scrapy.Field()
    Course_Content = scrapy.Field()
    Organisation_Name = scrapy.Field()


class RiceSpider(scrapy.Spider):
    name = 'myskillsfuture'
    # start_urls = ["https://www.myskillsfuture.sg/services/tex/individual/course-search?query=rows%3D24%26facet%3Dtrue%26facet.mincount%3D1%26json.nl%3Dmap%26facet.field%3D%257B!ex%253DCourse_Vacancy%257DCourse_Vacancy%26facet.field%3D%257B!ex%253DCourse_Vacancy%257DCourse_Vacancy_facet%26facet.field%3D%257B!ex%253DTP_ALIAS_Suggest%257DTP_ALIAS_Suggest%26facet.field%3D%257B!ex%253DWheelchair_Access%257DWheelchair_Access%26facet.field%3D%257B!ex%253DArea_of_Training%257DArea_of_Training%26facet.field%3D%257B!ex%253DArea_of_Training%257DArea_of_Training_facet%26facet.field%3D%257B!ex%253DJob_Level%257DJob_Level%26facet.field%3D%257B!ex%253DJob_Level%257DJob_Level_facet%26facet.field%3D%257B!ex%253DMode_of_Training%257DMode_of_Training%26facet.field%3D%257B!ex%253DMode_of_Training%257DMode_of_Training_facet%26facet.field%3D%257B!ex%253DMedium_of_Instruction%257DMedium_of_Instruction%26facet.field%3D%257B!ex%253DMedium_of_Instruction%257DMedium_of_Instruction_facet%26facet.field%3D%257B!ex%253DMinimum_Education_Req%257DMinimum_Education_Req%26facet.field%3D%257B!ex%253DMinimum_Education_Req%257DMinimum_Education_Req_facet%26facet.field%3D%257B!ex%253DCourse_Funding%257DCourse_Funding%26facet.field%3D%257B!ex%253DCourse_Funding%257DCourse_Funding_facet%26fq%3DCourse_Supp_Period_To_1%253A%255B2020-05-15T00%253A00%253A00Z%2520TO%2520*%255D%26fq%3DIsValid%253Atrue%26q%3D*%253A*%26start%3D1%26refresh%3D1589501304647"]
    start_urls = []
    for i in range(0, 21000, 24):
        url = "https://www.myskillsfuture.sg/services/tex/individual/course-search?query=rows%3D24%26facet%3Dtrue%26facet.mincount%3D1%26json.nl%3Dmap%26facet.field%3D%257B!ex%253DCourse_Vacancy%257DCourse_Vacancy%26facet.field%3D%257B!ex%253DCourse_Vacancy%257DCourse_Vacancy_facet%26facet.field%3D%257B!ex%253DTP_ALIAS_Suggest%257DTP_ALIAS_Suggest%26facet.field%3D%257B!ex%253DWheelchair_Access%257DWheelchair_Access%26facet.field%3D%257B!ex%253DArea_of_Training%257DArea_of_Training%26facet.field%3D%257B!ex%253DArea_of_Training%257DArea_of_Training_facet%26facet.field%3D%257B!ex%253DJob_Level%257DJob_Level%26facet.field%3D%257B!ex%253DJob_Level%257DJob_Level_facet%26facet.field%3D%257B!ex%253DMode_of_Training%257DMode_of_Training%26facet.field%3D%257B!ex%253DMode_of_Training%257DMode_of_Training_facet%26facet.field%3D%257B!ex%253DMedium_of_Instruction%257DMedium_of_Instruction%26facet.field%3D%257B!ex%253DMedium_of_Instruction%257DMedium_of_Instruction_facet%26facet.field%3D%257B!ex%253DMinimum_Education_Req%257DMinimum_Education_Req%26facet.field%3D%257B!ex%253DMinimum_Education_Req%257DMinimum_Education_Req_facet%26facet.field%3D%257B!ex%253DCourse_Funding%257DCourse_Funding%26facet.field%3D%257B!ex%253DCourse_Funding%257DCourse_Funding_facet%26fq%3DCourse_Supp_Period_To_1%253A%255B2020-05-15T00%253A00%253A00Z%2520TO%2520*%255D%26fq%3DIsValid%253Atrue%26q%3D*%253A*%26start%3D{}%26refresh%3D1589501304647".format(i)
        start_urls.append(url)
    
    def parse(self, response):
        jsonresponse = json.loads(response.text)
        item = MyItem()
        # with open("myskillsfuture.json", "w") as outfile:
            # json.dump(jsonresponse, outfile, indent=4, separators=(',',':'))
        for course in jsonresponse["grouped"]["GroupID"]["groups"]:
            item["EXT_Course_Ref_No"] = course["doclist"]["docs"][0]["EXT_Course_Ref_No"]
            item["Course_Title"] = course["doclist"]["docs"][0]["Course_Title"]
            item["Course_Objective"] = course["doclist"]["docs"][0]["Course_Objective"] 
            item["Course_Content"] = course["doclist"]["docs"][0]["Course_Content"]
            item["Organisation_Name"] = course["doclist"]["docs"][0]["Organisation_Name"]
            yield item
        # item["Course_Title"] = jsonresponse["Course_Title"]
        # item["Course_Objective"] = jsonresponse["Course_Objective"]
        # item["Organisation_Name"] = jsonresponse["Organisation_Name"]        

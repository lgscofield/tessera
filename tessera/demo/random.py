import json
import sys
from ..model import *
from ..model.database import *

def demo_random_data_dashboard():
    return database.Dashboard(
        title='Random Data',
        category='Demo',
        tags=[ Tag('demo'), Tag('random')],
        definition = DashboardDef(
            definition=dumps(
                DashboardDefinition(
                     queries = {
                         'cpu_usage' : 'absolute(group(randomWalkFunction("system"),randomWalkFunction("user"),randomWalkFunction("wait")))',
                         'cluster' : 'aliasByNode(absolute(group(randomWalkFunction("s001"),randomWalkFunction("s002"),randomWalkFunction("s003"),randomWalkFunction("s004"),randomWalkFunction("s005"))), 0)',
                         'thing1' : 'randomWalkFunction(thing1)',
                         'thing2' : 'randomWalkFunction(thing2)',
                         'thing3' : 'randomWalkFunction(thing3)',
                         'thing4' : 'randomWalkFunction(thing4)'
                     },
                     items=Section(layout=Section.Layout.FIXED,
                                   items=[
                                       Heading(text='A Heading',
                                               description='Followed by a separator')
                                       ,Separator()
                                       ,Row(items=[
                                           Cell(span=4,
                                                items=[
                                                    JumbotronSingleStat(title='Jumbotron Singlestat',
                                                                        query='cpu_usage',
                                                                        units='frobs')
                                                ])
                                           ,Cell(span=8, style=DashboardItem.Style.WELL,
                                                 items=StackedAreaChart(query='cpu_usage', height=3, title="stacked_area_chart"))
                                       ])
                                       ,Row(items=[
                                           Cell(span=3,offset=4,align='center', style=DashboardItem.Style.WELL,
                                                items=SingleStat(title='Max. Frob Density',
                                                                 query='cpu_usage',
                                                                 transform='max',
                                                                 units='frobs/kg',
                                                                 format=',.0f'))
                                           ,Cell(span=2,align='center',style=DashboardItem.Style.WELL,
                                                 items=SingleStat(title='Average Rate',
                                                                  query='cpu_usage',
                                                                  transform='mean',
                                                                  units='/sec',
                                                                  format=',.2f'))
                                           ,Cell(span=3, style=DashboardItem.Style.WELL,align='center',
                                                 items=SingleStat(title='Total Frobs',
                                                                  query='cpu_usage',
                                                                  transform='sum',
                                                                  units='frobs',
                                                                  format=',.0f'))
                                           ])
                                       ,Heading(text="Cluster Health",
                                                description="Very Important Metrics for Determining Things and Stuff",
                                                level=2)
                                       ,Separator()
                                       ,Row(items=[
                                           Cell(span=12,
                                                items=StandardTimeSeries(height=4,
                                                                         query='cluster',
                                                                         options={
                                                                             'yAxisLabel' : 'frobs per second',
                                                                             'margin' : {
                                                                                 'top' : 0, 'bottom' : 16, 'right' : 0, 'left' : 80
                                                                             }
                                                                         }))
                                           ])
                                       ,Row(items=[
                                           Cell(span=4,
                                                items=Markdown(text="### An Explanatory Box\n\n"
                                                               + "Containing text in [Markdown](https://daringfireball.net/projects/markdown/) format. "
                                                               + "You can use this to include explanatory text about your metrics. The table to the right "
                                                               + "is a ``summation_table`` presentation linked to the same query as the "
                                                               + "``standard_time_series`` presentation displayed above."))
                                           ,Cell(span=4,
                                                 items=SummationTable(query='cluster',
                                                                      format=',.4f'))
                                           ,Cell(span=4,
                                                 items=DonutChart(title='Distribution of Frobs',
                                                                  query='cluster'))
                                       ])
                                       ,Heading(text="Summaries")
                                       ,Separator()
                                       ,Row(items=[
                                           Cell(span=2,
                                                items=SingleStat(title='Max', transform='max', format=',.1f', units='things', query='thing1'))
                                           ,Cell(span=2,
                                                 items=SingleStat(title='Average', transform='mean', format=',.1f', units='things', query='thing1'))
                                           ,Cell(span=8,
                                                 items=SimpleTimeSeries(query='thing1'))
                                       ])
                                       ,Row(items=[
                                           Cell(span=2,
                                                items=SingleStat(title='Max', transform='max', format=',.1f', units='things', query='thing2'))
                                           ,Cell(span=2,
                                                 items=SingleStat(title='Average', transform='mean', format=',.1f', units='things', query='thing2'))
                                           ,Cell(span=8,
                                                 items=SimpleTimeSeries(query='thing2'))
                                       ])
                                       ,Row(items=[
                                           Cell(span=2,
                                                items=SingleStat(title='Max', transform='max', format=',.1f', units='things', query='thing3'))
                                           ,Cell(span=2,
                                                 items=SingleStat(title='Average', transform='mean', format=',.1f', units='things', query='thing3'))
                                           ,Cell(span=8,
                                                 items=SimpleTimeSeries(query='thing3'))
                                       ])
                                       ,Row(items=[
                                           Cell(span=2,
                                                items=SingleStat(title='Max', transform='max', format=',.1f', units='things', query='thing4'))
                                           ,Cell(span=2,
                                                 items=SingleStat(title='Average', transform='mean', format=',.1f', units='things', query='thing4'))
                                           ,Cell(span=8,
                                                 items=SimpleTimeSeries(query='thing4'))
                                       ])
                                   ])))))
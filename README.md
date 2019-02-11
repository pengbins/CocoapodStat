<h1 align="center" ><a href="https://pengbins.github.io/CocoapodStat">Cocoapods stat</a></h1>

[![Build Status](https://travis-ci.org/pengbins/CocoapodStat.svg?branch=master)](https://travis-ci.org/pengbins/CocoapodStat)


本项目里用 Cocoapods API + Travis CI + github pages + echarts 来自动统计一个 通过Cocoapods发布的SDK的使用情况.

* [Cocoapods metrics API](http://blog.cocoapods.org/metrics-api/)


>> http://metrics.cocoapods.org/api/v1/pods/<pod_name>


通过以上API, 可以查询到pod_name对应的SDK的各项指标

| 指标 | 说明 | 
| -- | -- |
| app_total | 使用过本SDK的app数量 |
| app_week| 本周使用过本SDK的app数量 |
| download_month| 本月SDK的下载次数 |
| download_total| SDK的下载总次数 |
| download_week| 本周SDK的下载次数 |

* Travis CI

使用Travis CI的[定时任务](https://docs.travis-ci.com/user/cron-jobs/), 每天调用一次 Cocoapods metrics API
并将获取到的数据更新到本仓库中

* github pages
通过 github pages 将Travis CI 收集到的数据展示在静态页面上

* 使用 echars 将数据用曲线的方式进行展示




<h1 align="center" ><a href="https://pengbins.github.io/CocoapodStat">Cocoapods stat</a></h1>

[![Build Status](https://travis-ci.org/pengbins/CocoapodStat.svg?branch=master)](https://travis-ci.org/pengbins/CocoapodStat)

Using Cocoapods API + Travis CI + github pages + echarts to track the usage data of a SDK

* [Cocoapods metrics API](http://blog.cocoapods.org/metrics-api/)

>> http://metrics.cocoapods.org/api/v1/pods/<pod_name>

By this API, the merics of pod_name is avaliable.

| metrics | desc | 
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



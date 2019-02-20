from get_index import BaiduIndex

if __name__ == "__main__":
    """
    最多一次请求5个关键词
    """
    # 查看城市和省份的对应代码
    print(BaiduIndex.city_code)
    print(BaiduIndex.province_code)

    baidu_index = BaiduIndex(['找工作', '失业', '裁员'], '2011-01-01', '2016-10-01')
    for data in baidu_index('找工作', 'all'):
        print(data)

    # 获取全部5个关键词的全部数据
   ## print(baidu_index.result)
    # 获取1个关键词的全部数据
    print(baidu_index.result['找工作'])
    # 获取1个关键词的移动端数据
   ## print(baidu_index.result['找工作']['wise'])
    # 获取1个关键词的pc端数据
   ## print(baidu_index.result['找工作']['pc'])

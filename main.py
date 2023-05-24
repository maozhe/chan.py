from Chan import CChan
from ChanConfig import CChanConfig
from Common.CEnum import AUTYPE, DATA_SRC, KL_TYPE
from Plot.AnimatePlotDriver import CAnimateDriver
from Plot.PlotDriver import CPlotDriver

if __name__ == "__main__":
    # code = "sz.000001"
    # code = "sh.600771" # 广誉远
    # code = "sz.002182" # 云海金属
    code = "sz.000636" # 风华高科
   # code = "sz.300253" # 卫宁健康

    begin_time = "2018-01-01"
    end_time = None
    data_src = DATA_SRC.BAO_STOCK  # 数据源
    # lv_list = [KL_TYPE.K_DAY]  # k线级别
    lv_list = [KL_TYPE.K_DAY, KL_TYPE.K_60M]  # k线级别

    config = CChanConfig({
        "bi_strict": True, # 是否只用严格笔(bi_algo=normal时有效)，默认为 Ture
        "bi_fx_check": "strict",
        "triger_step": False, # 是否回放逐步返回，默认为 False
        "skip_step": 0, # triger_step 为 True 时有效，指定跳过前面几根K线，默认为 0；
        "divergence_rate": float("inf"), # 1类买卖点背驰比例，即离开中枢的笔的 MACD 指标相对于进入中枢的笔，默认为 0.9
        "bsp2_follow_1": False, # 2类买卖点是否必须跟在1类买卖点后面（用于小转大时1类买卖点因为背驰度不足没生成），默认为 True
        "bsp3_follow_1": False, # 3类买卖点是否必须跟在1类买卖点后面（用于小转大时1类买卖点因为背驰度不足没生成），默认为 True
        "min_zs_cnt": 0,  # 1类买卖点至少要经历几个中枢，默认为 1
        "bs1_peak": False,  # 1类买卖点位置是否必须是整个中枢最低点，默认为 True
        "macd_algo": "peak", # MACD指标算法（可自定义）
        "bs_type": '1,2,3a,1p,2s,3b', # 关注的买卖点类型，逗号分隔，默认"1,1p,2,2s,3a,3b"
        "print_warning": True, # 打印K线不一致的明细，默认为 True
    })

    plot_config = {
        "plot_kline": True, # 画K线，默认为 False
        "plot_kline_combine": False,  # 画合并K线，默认为 False
        "plot_bi": True,  # 画笔，默认为 False
        "plot_seg": True, # 画线段，默认为 False
        "plot_eigen": False, # 画特征序列（一般调试用），默认为 False
        "plot_zs": True, # 画中枢，默认为 False
        "plot_macd": False, # 画 MACD 图（图片下方额外开一幅图），默认为 False
        "plot_mean": False,  # 画均线，默认为 False
        "plot_channel": False, # 画上下轨道，默认为 False
        "plot_bsp": True, # 画理论买卖点，默认为 False
        "plot_extrainfo": False,
        "plot_demark": False, # 绘制Demark指标
        "only_top_lv": False
    }

    plot_para = {
        "seg": {
        },
        "bi": {
            # "show_num": True,
            # "disp_end": True,
            "sub_lv_cnt": None,  # 次级别只画本级别的多少笔，None 即为全部
        },
        "figure": {
            "x_range": 250, # 0 最高级别绘制只画最后几根K线范围，为 0 表示不生效，绘制全部
        },
    }
    chan = CChan(
        code=code,
        begin_time=begin_time,
        end_time=end_time,
        data_src=data_src,
        lv_list=lv_list,
        config=config,
        autype=AUTYPE.QFQ,
    )

    if not config.triger_step:
        plot_driver = CPlotDriver(
            chan,
            plot_config=plot_config,
            plot_para=plot_para,
        )
        plot_driver.figure.show()
        print("ok");
    else:
        CAnimateDriver(
            chan,
            plot_config=plot_config,
            plot_para=plot_para,
        )

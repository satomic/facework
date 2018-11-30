import { $init, $digest } from '../../utils/common.util'

//index.js
//获取应用实例
const app = getApp()

Page({
  data: {
    imgUrls: [
      '/images/swiper_wjk.jpg',
      '/images/swiper_wy.jpg',
      '/images/swiper_yyqx.jpg',
    ],
    //是否采用衔接滑动  
    circular: true,
    //是否显示画板指示点  
    indicatorDots: true,
    //选中点的颜色  
    indicatorcolor: "#ccc",
    //是否竖直  
    vertical: false,
    //是否自动切换  
    autoplay: true,
    //自动切换的间隔
    interval: 3000,
    //滑动动画时长毫秒  
    duration: 1000,

    images: []
  },
  goToBattle: function(){
    wx: wx.navigateTo({
      url: '../battle/battle',
      success: function(res) {},
      fail: function(res) {},
      complete: function(res) {},
    })
  },

  // 选择图片及预览
  onLoad(options) {
    $init(this)
  },
  chooseImage(e) {
    wx.chooseImage({
      sizeType: ['original', 'compressed'],  //可选择原图或压缩后的图片
      sourceType: ['album', 'camera'], //可选择性开放访问相册、相机
      success: res => {
        const images = this.data.images.concat(res.tempFilePaths)
        // 限制最多只能留下3张照片
        this.data.images = images.length <= 3 ? images : images.slice(0, 3)
        $digest(this)
      }
    })
  },
  removeImage(e) {
    const idx = e.target.dataset.idx
    this.data.images.splice(idx, 1)
    $digest(this)
  },

  handleImagePreview(e) {
    const idx = e.target.dataset.idx
    const images = this.data.images
    wx.previewImage({
      current: images[idx],  //当前预览的图片
      urls: images,  //所有要预览的图片
    })
  }
})

let app = getApp();
Page({
  /**
   * 页面的初始数据
   */
  data: {
    isanswer: 1,
    sex:'/',
    age:0,
    yn:'/',
    yhm:app.data.yhm,
    content1:1,
    content2:2,
    content3:5,
    content4:4,
    content5:2,
    content6:3,
    content7:2,
    content8:2,
    content9:1,
    content10:3,
    content11:1,
    content12:4,
    content13:3,
    content14:2,
    content15:2,
    content16:3,
    content17:4,
    content18:2,
    content19:3,
    content20:4,
    content21:1,
    content22:3,
    content23:1,
    content24:4,
    content25:3,
    content26:2,
    content27:3,
    content28:5,
    content29:1,
    content30:5,
    content31:3,
    content32:1,
    content33:2,
    content34:3,
    content35:1,
    content36:'D',
    content37:'D',
    content38:'D',
    content39:'D',
    content40:'C',
    content41:'C',
    content42:'C',
    content43:'C',
    content44:'C',
    content45:'C',
    content46:'C',
    content47:'C',
    content48:'C',
    content49:'C',
    items: [
      {value: 'A', name: '0-30分钟'},
      {value: 'B', name: '30分钟-2小时'},
      {value: 'C', name: '2小时-4小时'},
      {value: 'D', name: '4小时以上'}
    ],
    ti40: [
      {value: 'A', name: '不作处理，直接出售'},
      {value: 'B', name: '将手机格式化，再进行出售'},
      {value: 'C', name: '将手机所有软件卸载掉'},
    ],
    ti41: [
      {value: 'A', name: '为了下载素材，使用微信扫描二维码'},
      {value: 'B', name: '不扫描二维码，关闭网站'},
      {value: 'C', name: '不扫描二维码，并举报该网站'},
    ],
    ti42: [
      {value: 'A', name: '拒绝填写信息'},
      {value: 'B', name: '有选择性地填写信息'},
      {value: 'C', name: '全部都填写'},
    ],
    ti43: [
      {value: 'A', name: '随手就打开了'},
      {value: 'B', name: '都知道我的名字一定要点开看'},
      {value: 'C', name: '先打电话向老师核实后再决定'},
    ],
    ti44: [
      {value: 'A', name: '点击查看，满足好奇心'},
      {value: 'B', name: '不点击，选择忽视'},
      {value: 'C', name: '向有关部门举报'},
    ],
    ti45: [
      {value: 'A', name: '提供相应信息'},
      {value: 'B', name: '联系预约医美机构，确认真实性'},
      {value: 'C', name: '忽视，视为骚扰'},
    ],
    ti46: [
      {value: 'A', name: '点开链接，了解里面的内容'},
      {value: 'B', name: '点开链接，随后填写相应信息'},
      {value: 'C', name: '登录铁路部门/航空部门官网/APP求证'},
    ],
    ti47: [
      {value: 'A', name: '提供个人信息'},
      {value: 'B', name: '怀疑对方，空闲时报警处理'},
      {value: 'C', name: '不提供，并选择忽视'},
    ],
    ti48: [
      {value: 'A', name: '电话'},
      {value: 'B', name: '邮件、短信'},
      {value: 'C', name: '其他方法'},
    ],
    ti49: [
      {value: 'A', name: '说法正确'},
      {value: 'B', name: '说法错误'},
      {value: 'C', name: '不确定'},
    ],
  },

  //第36题
  radioChange36(e) {
    console.log('36，携带value值为：', e.detail.value)
    this.data.content36 = e.detail.value
    const items = this.data.items
    for (let i = 0, len = items.length; i < len; ++i) {
      items[i].checked = items[i].value === e.detail.value
    }
    console.log(this.data.content36)
  },
  //第37题
  radioChange37(e) {
    console.log('37，携带value值为：', e.detail.value)
    this.data.content37 = e.detail.value
    const items = this.data.items
    for (let i = 0, len = items.length; i < len; ++i) {
      items[i].checked = items[i].value === e.detail.value
    }
    console.log(this.data.content37)
  },
    //第38题
    radioChange38(e) {
      console.log('38，携带value值为：', e.detail.value)
      this.data.content38 = e.detail.value
      const items = this.data.items
      for (let i = 0, len = items.length; i < len; ++i) {
        items[i].checked = items[i].value === e.detail.value
      }
      console.log(this.data.content38)
    },
     //第39题
     radioChange39(e) {
      console.log('39，携带value值为：', e.detail.value)
      this.data.content39 = e.detail.value
      const items = this.data.items
      for (let i = 0, len = items.length; i < len; ++i) {
        items[i].checked = items[i].value === e.detail.value
      }
      console.log(this.data.content39)
    },
    radioChange40(e) {
      console.log('40，携带value值为：', e.detail.value)
      this.data.content40 = e.detail.value
      const items = this.data.items
      for (let i = 0, len = items.length; i < len; ++i) {
        items[i].checked = items[i].value === e.detail.value
      }
      console.log(this.data.content40)
    },
    radioChange41(e) {
      console.log('41，携带value值为：', e.detail.value)
      this.data.content41 = e.detail.value
      const items = this.data.items
      for (let i = 0, len = items.length; i < len; ++i) {
        items[i].checked = items[i].value === e.detail.value
      }
      console.log(this.data.content41)
    },
    radioChange42(e) {
      console.log('42，携带value值为：', e.detail.value)
      this.data.content42 = e.detail.value
      const items = this.data.items
      for (let i = 0, len = items.length; i < len; ++i) {
        items[i].checked = items[i].value === e.detail.value
      }
      console.log(this.data.content42)
    },
    radioChange43(e) {
      console.log('43，携带value值为：', e.detail.value)
      this.data.content43 = e.detail.value
      const items = this.data.items
      for (let i = 0, len = items.length; i < len; ++i) {
        items[i].checked = items[i].value === e.detail.value
      }
      console.log(this.data.content43)
    },
    radioChange44(e) {
      console.log('44，携带value值为：', e.detail.value)
      this.data.content44 = e.detail.value
      const items = this.data.items
      for (let i = 0, len = items.length; i < len; ++i) {
        items[i].checked = items[i].value === e.detail.value
      }
      console.log(this.data.content44)
    },
    radioChange45(e) {
      console.log('45，携带value值为：', e.detail.value)
      this.data.content45 = e.detail.value
      const items = this.data.items
      for (let i = 0, len = items.length; i < len; ++i) {
        items[i].checked = items[i].value === e.detail.value
      }
      console.log(this.data.content45)
    },
    radioChange46(e) {
      console.log('46，携带value值为：', e.detail.value)
      this.data.content46 = e.detail.value
      const items = this.data.items
      for (let i = 0, len = items.length; i < len; ++i) {
        items[i].checked = items[i].value === e.detail.value
      }
      console.log(this.data.content46)
    },
    radioChange47(e) {
      console.log('47，携带value值为：', e.detail.value)
      this.data.content47 = e.detail.value
      const items = this.data.items
      for (let i = 0, len = items.length; i < len; ++i) {
        items[i].checked = items[i].value === e.detail.value
      }
      console.log(this.data.content47)
    },
    radioChange48(e) {
      console.log('48，携带value值为：', e.detail.value)
      this.data.content48 = e.detail.value
      const items = this.data.items
      for (let i = 0, len = items.length; i < len; ++i) {
        items[i].checked = items[i].value === e.detail.value
      }
      console.log(this.data.content48)
    },
    radioChange49(e) {
      console.log('49，携带value值为：', e.detail.value)
      this.data.content49 = e.detail.value
      const items = this.data.items
      for (let i = 0, len = items.length; i < len; ++i) {
        items[i].checked = items[i].value === e.detail.value
      }
      console.log(this.data.content49)
    },
  //第一部分 基本信息
  sex1:function(){
    console.log('sex1:男')
    this.setData({
      sex:'男'
    })
  },
  sex2:function(){
    console.log('sex2:女')
    this.setData({
      sex:'女'
    })
  },
  age(e){
    this.setData({
      age:e.detail.value
    })
    console.log('年龄',this.data.age)
  },
  yn1:function(){
    console.log('yn1:是')
    this.setData({
      yn:'是'
    })
  },
  yn2:function(){
    console.log('yn2:否')
    this.setData({
      yn:'否'
    })
  },
  //第二部分
  //第1题
  change1a:function(){
    console.log('1-1')
    this.setData({
      content1:'1'
    })
  },
  change1b:function(){
    console.log('1-2')
    this.setData({
      content1:'2'
    })
  },
  change1c:function(){
    console.log('1-3')
    this.setData({
      content1:'3'
    })
  },
  change1d:function(){
    console.log('1-4')
    this.setData({
      content1:'4'
    })
  },
  change1e:function(){
    console.log('1-5')
    this.setData({
      content1:'5'
    })
  },
  //第2题
  change2a:function(){
    console.log('2-1')
    this.setData({
      content2:'1'
    })
  },
  change2b:function(){
    console.log('2-2')
    this.setData({
      content2:'2'
    })
  },
  change2c:function(){
    console.log('2-3')
    this.setData({
      content2:'3'
    })
  },
  change2d:function(){
    console.log('2-4')
    this.setData({
      content2:'4'
    })
  },
  change2e:function(){
    console.log('2-5')
    this.setData({
      content2:'5'
    })
  },
  //第3题
  change3a:function(){
    console.log('3-1')
    this.setData({
      content3:'1'
    })
  },
  change3b:function(){
    console.log('3-2')
    this.setData({
      content3:'2'
    })
  },
  change3c:function(){
    console.log('3-3')
    this.setData({
      content3:'3'
    })
  },
  change3d:function(){
    console.log('3-4')
    this.setData({
      content3:'4'
    })
  },
  change3e:function(){
    console.log('3-5')
    this.setData({
      content3:'5'
    })
  },
  //第4题
  change4a:function(){
    console.log('4-1')
    this.setData({
      content4:'1'
    })
  },
  change4b:function(){
    console.log('4-2')
    this.setData({
      content4:'2'
    })
  },
  change4c:function(){
    console.log('4-3')
    this.setData({
      content4:'3'
    })
  },
  change4d:function(){
    console.log('4-4')
    this.setData({
      content4:'4'
    })
  },
  change4e:function(){
    console.log('4-5')
    this.setData({
      content4:'5'
    })
  },
  //第5题
  change5a:function(){
    console.log('5-1')
    this.setData({
      content5:'1'
    })
  },
  change5b:function(){
    console.log('5-2')
    this.setData({
      content5:'2'
    })
  },
  change5c:function(){
    console.log('5-3')
    this.setData({
      content5:'3'
    })
  },
  change5d:function(){
    console.log('5-4')
    this.setData({
      content5:'4'
    })
  },
  change5e:function(){
    console.log('5-5')
    this.setData({
      content5:'5'
    })
  },
  //第6题
  change6a:function(){
    console.log('6-1')
    this.setData({
      content6:'1'
    })
  },
  change6b:function(){
    console.log('6-2')
    this.setData({
      content6:'2'
    })
  },
  change6c:function(){
    console.log('6-3')
    this.setData({
      content6:'3'
    })
  },
  change6d:function(){
    console.log('6-4')
    this.setData({
      content6:'4'
    })
  },
  change6e:function(){
    console.log('6-5')
    this.setData({
      content6:'5'
    })
  },
  //第7题
  change7a:function(){
    console.log('7-1')
    this.setData({
      content7:'1'
    })
  },
  change7b:function(){
    console.log('7-2')
    this.setData({
      content7:'2'
    })
  },
  change7c:function(){
    console.log('7-3')
    this.setData({
      content7:'3'
    })
  },
  change7d:function(){
    console.log('7-4')
    this.setData({
      content7:'4'
    })
  },
  change7e:function(){
    console.log('7-5')
    this.setData({
      content7:'5'
    })
  },
  //第8题 
  change8a:function(){
    console.log('8-1')
    this.setData({
      content8:'1'
    })
  },
  change8b:function(){
    console.log('8-2')
    this.setData({
      content8:'2'
    })
  },
  change8c:function(){
    console.log('8-3')
    this.setData({
      content8:'3'
    })
  },
  change8d:function(){
    console.log('8-4')
    this.setData({
      content8:'4'
    })
  },
  change8e:function(){
    console.log('8-5')
    this.setData({
      content8:'5'
    })
  },
  //第9题
  change9a:function(){
    console.log('9-1')
    this.setData({
      content9:'1'
    })
  },
  change9b:function(){
    console.log('9-2')
    this.setData({
      content9:'2'
    })
  },
  change9c:function(){
    console.log('9-3')
    this.setData({
      content9:'3'
    })
  },
  change9d:function(){
    console.log('9-4')
    this.setData({
      content9:'4'
    })
  },
  change9e:function(){
    console.log('9-5')
    this.setData({
      content9:'5'
    })
  },
  //第10题
  change10a:function(){
    console.log('10-1')
    this.setData({
      content10:'1'
    })
  },
  change10b:function(){
    console.log('10-2')
    this.setData({
      content10:'2'
    })
  },
  change10c:function(){
    console.log('10-3')
    this.setData({
      content10:'3'
    })
  },
  change10d:function(){
    console.log('10-4')
    this.setData({
      content10:'4'
    })
  },
  change10e:function(){
    console.log('10-5')
    this.setData({
      content10:'5'
    })
  },
  //第11题
  change11a:function(){
    console.log('11-1')
    this.setData({
      content11:'1'
    })
  },
  change11b:function(){
    console.log('11-2')
    this.setData({
      content11:'2'
    })
  },
  change11c:function(){
    console.log('11-3')
    this.setData({
      content11:'3'
    })
  },
  change11d:function(){
    console.log('11-4')
    this.setData({
      content11:'4'
    })
  },
  change11e:function(){
    console.log('11-5')
    this.setData({
      content11:'5'
    })
  },
  //第12题
  change12a:function(){
    console.log('12-1')
    this.setData({
      content12:'1'
    })
  },
  change12b:function(){
    console.log('12-2')
    this.setData({
      content12:'2'
    })
  },
  change12c:function(){
    console.log('12-3')
    this.setData({
      content12:'3'
    })
  },
  change12d:function(){
    console.log('12-4')
    this.setData({
      content12:'4'
    })
  },
  change12e:function(){
    console.log('12-5')
    this.setData({
      content12:'5'
    })
  },
  //第13题
  change13a:function(){
    console.log('13-1')
    this.setData({
      content13:'1'
    })
  },
  change13b:function(){
    console.log('13-2')
    this.setData({
      content13:'2'
    })
  },
  change13c:function(){
    console.log('13-3')
    this.setData({
      content13:'3'
    })
  },
  change13d:function(){
    console.log('13-4')
    this.setData({
      content13:'4'
    })
  },
  change13e:function(){
    console.log('13-5')
    this.setData({
      content13:'5'
    })
  },
  //第14题
  change14a:function(){
    console.log('14-1')
    this.setData({
      content14:'1'
    })
  },
  change14b:function(){
    console.log('14-2')
    this.setData({
      content14:'2'
    })
  },
  change14c:function(){
    console.log('14-3')
    this.setData({
      content14:'3'
    })
  },
  change14d:function(){
    console.log('14-4')
    this.setData({
      content14:'4'
    })
  },
  change14e:function(){
    console.log('14-5')
    this.setData({
      content14:'5'
    })
  },
  //第15题
  change15a:function(){
    console.log('15-1')
    this.setData({
      content15:'1'
    })
  },
  change15b:function(){
    console.log('15-2')
    this.setData({
      content15:'2'
    })
  },
  change15c:function(){
    console.log('15-3')
    this.setData({
      content15:'3'
    })
  },
  change15d:function(){
    console.log('15-4')
    this.setData({
      content15:'4'
    })
  },
  change15e:function(){
    console.log('15-5')
    this.setData({
      content15:'5'
    })
  },
  //第16题
  change16a:function(){
    console.log('16-1')
    this.setData({
      content16:'1'
    })
  },
  change16b:function(){
    console.log('16-2')
    this.setData({
      content16:'2'
    })
  },
  change16c:function(){
    console.log('16-3')
    this.setData({
      content16:'3'
    })
  },
  change16d:function(){
    console.log('16-4')
    this.setData({
      content16:'4'
    })
  },
  change16e:function(){
    console.log('16-5')
    this.setData({
      content16:'5'
    })
  },
  //第17题
  change17a:function(){
    console.log('17-1')
    this.setData({
      content17:'1'
    })
  },
  change17b:function(){
    console.log('17-2')
    this.setData({
      content17:'2'
    })
  },
  change17c:function(){
    console.log('17-3')
    this.setData({
      content17:'3'
    })
  },
  change17d:function(){
    console.log('17-4')
    this.setData({
      content17:'4'
    })
  },
  change17e:function(){
    console.log('17-5')
    this.setData({
      content17:'5'
    })
  },
  //第18题 
  change18a:function(){
    console.log('18-1')
    this.setData({
      content18:'1'
    })
  },
  change18b:function(){
    console.log('18-2')
    this.setData({
      content18:'2'
    })
  },
  change18c:function(){
    console.log('18-3')
    this.setData({
      content18:'3'
    })
  },
  change18d:function(){
    console.log('18-4')
    this.setData({
      content18:'4'
    })
  },
  change18e:function(){
    console.log('18-5')
    this.setData({
      content18:'5'
    })
  },
  //第19题
  change19a:function(){
    console.log('19-1')
    this.setData({
      content19:'1'
    })
  },
  change19b:function(){
    console.log('19-2')
    this.setData({
      content19:'2'
    })
  },
  change19c:function(){
    console.log('19-3')
    this.setData({
      content19:'3'
    })
  },
  change19d:function(){
    console.log('19-4')
    this.setData({
      content19:'4'
    })
  },
  change19e:function(){
    console.log('19-5')
    this.setData({
      content19:'5'
    })
  },
  //第20题
  change20a:function(){
    console.log('20-1')
    this.setData({
      content20:'1'
    })
  },
  change20b:function(){
    console.log('20-2')
    this.setData({
      content20:'2'
    })
  },
  change20c:function(){
    console.log('20-3')
    this.setData({
      content20:'3'
    })
  },
  change20d:function(){
    console.log('20-4')
    this.setData({
      content20:'4'
    })
  },
  change20e:function(){
    console.log('20-5')
    this.setData({
      content20:'5'
    })
  },
  //第21题
  change21a:function(){
    console.log('21-1')
    this.setData({
      content21:'1'
    })
  },
  change21b:function(){
    console.log('21-2')
    this.setData({
      content21:'2'
    })
  },
  change21c:function(){
    console.log('21-3')
    this.setData({
      content21:'3'
    })
  },
  change21d:function(){
    console.log('21-4')
    this.setData({
      content21:'4'
    })
  },
  change21e:function(){
    console.log('21-5')
    this.setData({
      content21:'5'
    })
  },
  //第2题
  change22a:function(){
    console.log('22-1')
    this.setData({
      content22:'1'
    })
  },
  change22b:function(){
    console.log('22-2')
    this.setData({
      content22:'2'
    })
  },
  change22c:function(){
    console.log('22-3')
    this.setData({
      content22:'3'
    })
  },
  change22d:function(){
    console.log('22-4')
    this.setData({
      content22:'4'
    })
  },
  change22e:function(){
    console.log('22-5')
    this.setData({
      content22:'5'
    })
  },
  //第3题
  change23a:function(){
    console.log('23-1')
    this.setData({
      content23:'1'
    })
  },
  change23b:function(){
    console.log('23-2')
    this.setData({
      content23:'2'
    })
  },
  change23c:function(){
    console.log('23-3')
    this.setData({
      content23:'3'
    })
  },
  change23d:function(){
    console.log('23-4')
    this.setData({
      content23:'4'
    })
  },
  change23e:function(){
    console.log('23-5')
    this.setData({
      content23:'5'
    })
  },
  //第24题
  change24a:function(){
    console.log('24-1')
    this.setData({
      content24:'1'
    })
  },
  change24b:function(){
    console.log('24-2')
    this.setData({
      content24:'2'
    })
  },
  change24c:function(){
    console.log('24-3')
    this.setData({
      content24:'3'
    })
  },
  change24d:function(){
    console.log('24-4')
    this.setData({
      content24:'4'
    })
  },
  change24e:function(){
    console.log('24-5')
    this.setData({
      content24:'5'
    })
  },
  //第25题
  change25a:function(){
    console.log('25-1')
    this.setData({
      content25:'1'
    })
  },
  change25b:function(){
    console.log('25-2')
    this.setData({
      content25:'2'
    })
  },
  change25c:function(){
    console.log('25-3')
    this.setData({
      content25:'3'
    })
  },
  change25d:function(){
    console.log('25-4')
    this.setData({
      content25:'4'
    })
  },
  change25e:function(){
    console.log('25-5')
    this.setData({
      content25:'5'
    })
  },
  //第26题
  change26a:function(){
    console.log('26-1')
    this.setData({
      content26:'1'
    })
  },
  change26b:function(){
    console.log('26-2')
    this.setData({
      content26:'2'
    })
  },
  change26c:function(){
    console.log('26-3')
    this.setData({
      content26:'3'
    })
  },
  change26d:function(){
    console.log('26-4')
    this.setData({
      content26:'4'
    })
  },
  change26e:function(){
    console.log('26-5')
    this.setData({
      content26:'5'
    })
  },
  //第27题
  change27a:function(){
    console.log('27-1')
    this.setData({
      content27:'1'
    })
  },
  change27b:function(){
    console.log('27-2')
    this.setData({
      content27:'2'
    })
  },
  change27c:function(){
    console.log('27-3')
    this.setData({
      content27:'3'
    })
  },
  change27d:function(){
    console.log('27-4')
    this.setData({
      content27:'4'
    })
  },
  change27e:function(){
    console.log('27-5')
    this.setData({
      content27:'5'
    })
  },
  //第8题 
  change28a:function(){
    console.log('28-1')
    this.setData({
      content28:'1'
    })
  },
  change28b:function(){
    console.log('28-2')
    this.setData({
      content28:'2'
    })
  },
  change28c:function(){
    console.log('28-3')
    this.setData({
      content28:'3'
    })
  },
  change28d:function(){
    console.log('28-4')
    this.setData({
      content28:'4'
    })
  },
  change28e:function(){
    console.log('28-5')
    this.setData({
      content28:'5'
    })
  },
  //第9题
  change29a:function(){
    console.log('29-1')
    this.setData({
      content29:'1'
    })
  },
  change29b:function(){
    console.log('29-2')
    this.setData({
      content29:'2'
    })
  },
  change29c:function(){
    console.log('29-3')
    this.setData({
      content29:'3'
    })
  },
  change29d:function(){
    console.log('29-4')
    this.setData({
      content29:'4'
    })
  },
  change29e:function(){
    console.log('29-5')
    this.setData({
      content29:'5'
    })
  },
  //第30题
  change30a:function(){
    console.log('30-1')
    this.setData({
      content30:'1'
    })
  },
  change30b:function(){
    console.log('30-2')
    this.setData({
      content30:'2'
    })
  },
  change30c:function(){
    console.log('30-3')
    this.setData({
      content30:'3'
    })
  },
  change30d:function(){
    console.log('30-4')
    this.setData({
      content30:'4'
    })
  },
  change30e:function(){
    console.log('30-5')
    this.setData({
      content30:'5'
    })
  },
  //第31题
  change31a:function(){
    console.log('31-1')
    this.setData({
      content31:'1'
    })
  },
  change31b:function(){
    console.log('31-2')
    this.setData({
      content31:'2'
    })
  },
  change31c:function(){
    console.log('31-3')
    this.setData({
      content31:'3'
    })
  },
  change31d:function(){
    console.log('31-4')
    this.setData({
      content31:'4'
    })
  },
  change31e:function(){
    console.log('31-5')
    this.setData({
      content31:'5'
    })
  },
  //第2题
  change32a:function(){
    console.log('32-1')
    this.setData({
      content32:'1'
    })
  },
  change32b:function(){
    console.log('32-2')
    this.setData({
      content32:'2'
    })
  },
  change32c:function(){
    console.log('32-3')
    this.setData({
      content32:'3'
    })
  },
  change32d:function(){
    console.log('32-4')
    this.setData({
      content32:'4'
    })
  },
  change32e:function(){
    console.log('32-5')
    this.setData({
      content32:'5'
    })
  },
  //第33题
  change33a:function(){
    console.log('33-1')
    this.setData({
      content33:'1'
    })
  },
  change33b:function(){
    console.log('33-2')
    this.setData({
      content33:'2'
    })
  },
  change33c:function(){
    console.log('33-3')
    this.setData({
      content33:'3'
    })
  },
  change33d:function(){
    console.log('33-4')
    this.setData({
      content33:'4'
    })
  },
  change33e:function(){
    console.log('33-5')
    this.setData({
      content33:'5'
    })
  },
  //第34题
  change34a:function(){
    console.log('34-1')
    this.setData({
      content34:'1'
    })
  },
  change34b:function(){
    console.log('34-2')
    this.setData({
      content34:'2'
    })
  },
  change34c:function(){
    console.log('34-3')
    this.setData({
      content34:'3'
    })
  },
  change34d:function(){
    console.log('34-4')
    this.setData({
      content34:'4'
    })
  },
  change34e:function(){
    console.log('34-5')
    this.setData({
      content34:'5'
    })
  },
  //第35题
  change35a:function(){
    console.log('35-1')
    this.setData({
      content35:'1'
    })
  },
  change35b:function(){
    console.log('35-2')
    this.setData({
      content35:'2'
    })
  },
  change35c:function(){
    console.log('35-3')
    this.setData({
      content35:'3'
    })
  },
  change35d:function(){
    console.log('35-4')
    this.setData({
      content35:'4'
    })
  },
  change35e:function(){
    console.log('35-5')
    this.setData({
      content35:'5'
    })
  },
  
  
  //以下是翻页的代码
  next: function (event) {
    var that = this
    that.setData({
      isanswer: 2
    })
  },
  front: function (event) {
    var that = this
    that.setData({
      isanswer: 1
    })
  },
  front1: function (event) {
    var that = this
    that.setData({
      isanswer: 2
    })
  },
  front2: function (event) {
    var that = this
    that.setData({
      isanswer: 3
    })
  },
  front3: function (event) {
    var that = this
    that.setData({
      isanswer: 4
    })
  },
  //第一部分跳第二部分
  next2: function (event) {
    var that = this
    //三道题都写了才跳转（没有实现）
    if(this.sex!=' ' && this.age!=' ' && this.yn!=' '){
      that.setData({
        isanswer: 3
      })
    }else{
      wx.showToast({
        title: '请检查问题是否填写完整',
        icon: 'error'
      })
    }
  },
  //3转4
  next3: function (event) {
    var that = this
    that.setData({
      isanswer: 4
    })
  },
  //4转5
  next4: function (event) {
    var that = this
    that.setData({
      isanswer: 5
    })
  },

  backtologin: function (event) {
    wx.navigateTo({
      url: '../login/login',
    })
  },
  end: function (event) {
    var that = this
    that.setData({
      isanswer: 6
    })
    wx.request({
      method:'POST',
      url:'https://rbxerg.top/que',
      data: {
        sex:this.data.sex,
        age:this.data.age,
        yn:this.data.yn,
        yhm:app.globalData.yhm,
        content1:this.data.content1,
        content2:this.data.content2,
        content3:this.data.content3,
        content4:this.data.content4,
        content5:this.data.content5,
        content6:this.data.content6,
        content7:this.data.content7,
        content8:this.data.content8,
        content9:this.data.content9,
        content10:this.data.content10,
        content11:this.data.content11,
        content12:this.data.content12,
        content13:this.data.content13,
        content14:this.data.content14,
        content15:this.data.content15,
        content16:this.data.content16,
        content17:this.data.content17,
        content18:this.data.content18,
        content19:this.data.content19,
        content20:this.data.content20,
        content21:this.data.content21,
        content22:this.data.content22,
        content23:this.data.content23,
        content24:this.data.content24,
        content25:this.data.content25,
        content26:this.data.content26,
        content27:this.data.content27,
        content28:this.data.content28,
        content29:this.data.content29,
        content30:this.data.content30,
        content31:this.data.content31,
        content32:this.data.content32,
        content33:this.data.content33,
        content34:this.data.content34,
        content35:this.data.content35,
        content36:this.data.content36,
        content37:this.data.content37,
        content38:this.data.content38,
        content39:this.data.content39,
        content40:this.data.content40,
        content41:this.data.content41,
        content42:this.data.content42,
        content43:this.data.content43,
        content44:this.data.content44,
        content45:this.data.content45,
        content46:this.data.content46,
        content47:this.data.content47,
        content48:this.data.content48,
        content49:this.data.content49,
  
      },
      header: {
        'content-type': 'application/json' // 默认值
      },
      // response
      success: (res)=> {
        console.log(res.data)
        //这个地方的that是最上面定义的this，理解
      }
    })
  },
  onLoad:function (options) {
    console.log(app.data.yhm)
  }
})
//创建和初始化地图函数：
function initMap(){
  createMap();//创建地图
  setMapEvent();//设置地图事件
  addMapControl();//向地图添加控件
  addMapOverlay();//向地图添加覆盖物
}
function createMap(){
  map = new BMap.Map("contact");
  map.centerAndZoom(new BMap.Point(116.358853,39.991619),15);
}
function setMapEvent(){
  // map.enableScrollWheelZoom();
  map.enableKeyboard();
  map.enableDragging();
  map.enableDoubleClickZoom()
}
function addClickHandler(target,window){
  target.addEventListener("click", function(){
    target.openInfoWindow(window);
  });
}

function addMapOverlay(){
  var addr = {
    content: "北京市海淀区学院路35号世宁大厦902",
    title: "公司位置",
    imageOffset: {width:0, height:3},
    position: {lat:39.991751, lng:116.358822}
  };
  var point = new BMap.Point(addr.position.lng, addr.position.lat);
  var marker = new BMap.Marker(point,{icon:new BMap.Icon("http://api.map.baidu.com/lbsapi/createmap/images/icon.png",new BMap.Size(20,25),{
    imageOffset: new BMap.Size(addr.imageOffset.width, addr.imageOffset.height)
  })});
  var opts = {
    width: 200,
    title: addr.title,
    enableMessage: false
  };
  var infoWindow = new BMap.InfoWindow(addr.content, opts);
  addClickHandler(marker,infoWindow);
  map.addOverlay(marker);
  marker.openInfoWindow(infoWindow);
}
//向地图添加控件
function addMapControl(){
  var scaleControl = new BMap.ScaleControl({anchor:BMAP_ANCHOR_BOTTOM_LEFT});
  scaleControl.setUnit(BMAP_UNIT_IMPERIAL);
  map.addControl(scaleControl);
  var navControl = new BMap.NavigationControl({anchor:BMAP_ANCHOR_TOP_LEFT,type:BMAP_NAVIGATION_CONTROL_LARGE});
  map.addControl(navControl);
  var overviewControl = new BMap.OverviewMapControl({anchor:BMAP_ANCHOR_BOTTOM_RIGHT,isOpen:true});
  map.addControl(overviewControl);
}
var map;
  initMap();
---
title: "SP - Hasselblad 503cx Repair Diary"
excerpt: "Hasselblad 503cx Repair Diary (Sample Images Updated)<br/><img src='/images/album/hassel/503cx.jpeg' width=500px margin-top=20px>"
# excerpt: "TOKYO on FILM<br/><img src='/images/album/tokyo/shinjuku.jpeg' width=500px margin-top=20px>"
collection: portfolio
permalink: /portfolio/hassel25.html
date: 2025-03-14
---



```
免责声明：本文仅提供个人的哈苏相机维修经验，不保证专业性准确性，如按指示遇到问题，作者概不负责。
```


哈苏这个品牌在相机行业的积累实际上十分有限，近些年的营销将其抬升到了一个本不属于他的高度。某种意义上讲哈苏很难与徕卡的历史地位对等，但在今日的中文摄影圈，哈苏徕卡因为其相似的营销策略成为了奢侈品相机的代名词。若收起对营销手段的批判，不得不说哈苏与徕卡在胶片时代纯机械相机的设计比较优秀，分别在中画幅和135画幅的市场上有着不可撼动的历史地位。


本文给出哈苏503cx型号的一些维修经验，希望能帮到刷到这个帖子的有缘人。在维修开始前，先给所有出现故障的玩家们一个提醒：哈苏胶片机的一切操作逻辑都是先上弦（过片）。镜头要先机身上弦才能拆装、后背也需要在机身上弦后连接。关于机身的功能介绍，可以参考[Hasselblad 503cx & 500C/M Manual](http://www.hasselbladhistorical.eu/pdf/hasmanuals/503cx.pdf)。此外，希望在动手拆解前，各位可以先看完参考资料中列出的视频，对哈苏的内部结构有一个初步的认识。

# 问题描述

广泛地说，哈苏相机出现的问题主要是机身快门卡死，附属问题可能有后帘无法关闭、反光板预升出错等。笔者遇到的问题是过片若干次后出现上弦卸力、导致下次快门后没有充分回弹，进而导致后续快门卡死。虽然遇到的现象不尽相同，但解决方案大同小异。

# 拆解流程

哈苏胶片机的底层逻辑之一是上弦后拆装镜头，因此在机身卡死后，镜头也因为没有上弦而无法拆下。如图所示，机身下侧可以看到银色的旋钮，与镜头下侧的黑色旋钮对应。机身上弦会通过这个旋钮联动镜头上弦，在两侧都上满弦后，镜头才可以不被限位地安装/卸下。镜头旋钮旁边的小金属机构是快门释放开关，机身释放快门时，银色旋钮附近的机构会向外伸出，带动镜头释放快门。

<div>
    <img class="postimg" src="/images/album/hassel/bodynlens.jpg" width="450px" />
    <div class="caption">哈苏机身和镜头示意图 | <a href="https://www.japancamerahunter.com/product/hasselblad-500c-c80-2-8-a12ii/
    " target="_blank">图源</a></div>
</div>

为了能够拆解镜头，我们首先需要张开机身后面的两块幕帘，然后拆掉银色螺丝旁边的黑色螺丝，取下小的防尘罩。取下后可以看到右侧的两个小螺丝，我们交替操作拧松左侧稍大的螺丝并紧固右侧更小的螺丝，几轮操作后，镜头就可以被拆下。如果快门已经释放，镜头没有上弦，可以用镜头笔或者更大的一字螺丝刀，手动给镜头上弦，方便后续维修后装回。

类似上图中的机械结构设计从最早的500系列就已经固定，不同的具体型号均可以参考。但是500系列的拆解，随着后续机型功能的完善，会变得越来越复杂。503cx属于较为后期的型号，拆解时相比500c需要额外注意一些细节，这里推荐参考一些拆解视频[^1]$${}^,$$[^2]。

相比之前的500系列，503cx左侧机身增加了ISO拨盘和一个OTF测光接口。ISO拨盘需要移除表面的饰皮后拆解，OTF测光接口需要移除左下角部分饰皮拆解。由于这个接口是从内部固定，因此我们需要先将其向内推入，防止其卡住机身外壳。这部分可以参考视频[^2]中的1:10处。

机身右侧是标准的过片旋钮，拉开手柄后按住中间的按钮，逆时针转动即可拆下塑料手柄。内部的进一步拆解可以参考视频[^1]中的3:15处。

机身下侧是快拆板和外壳与内部的锚定螺丝。通过一个标准的一字螺丝刀可以非常快速拆解，这里提示记好螺丝位置，及时拍照或录像以防忘记。

此时机身应该能够被直接从金属框架中推出，参考视频中均有该流程，此处不再赘述。

<div>
    <img class="postimg" src="/images/album/hassel/503cx.jpeg" width="450px" />
    <div class="caption">500cx 内部与机身外壳分离</div>
</div>

分离后的内部结构相对简洁，比起Pentax和Nikon之类的135画幅机型，哈苏的机械结构甚至都要更加简单，当然这也得益于哈苏的模块化设计思路，许多机构被分散到了镜头和后背上，这样手动维修起来也会更加方便。

<div>
    <img class="postimg" src="/images/album/hassel/inner.jpeg" width="450px" />
    <div class="caption">500cx 内部主要结构</div>
</div>

这个图是我在拆开的第一时间拍摄的，可以看出第二个齿轮的螺丝根本没有拧紧，这可能是上次维修师傅粗心或不专业导致的。这就是导致我这次卡死的元凶。首先观察机身，边缘露出在机身之外的缺口齿轮实际上说明机身上弦分为两步，前半程主要是过片与部分机构联动，这部分上弦过程并不费力。当缺口部分齿轮转到内部时，后续上弦过程明显更费力，因为此时才是反光板回落、快门弹簧上劲的过程。上弦后释放快门，最外侧露出边缘的齿轮内部的平板弹簧会带动部分机构回转复位，从而准备下一次上弦。一个快门释放的视频可以在[这里](https://www.bilibili.com/video/BV1LfQSYMEPM)找到。

本次遇到的问题就是中间齿轮松脱，导致在上弦半圈后脱扣，使后续联动错误，从而影响后续上弦流程。此外，齿轮内部的弹簧也出现了松脱，这导致后续回弹无力，从而影响后帘和反光板复位的正常运作。

<mark>以下操作不建议初次维修者尝试</mark>

为了解决齿轮联动松脱的问题，我们在对齐齿孔（让缺口的齿轮在上弦/复位状态时缺口与机身外缘平行[^3]，参考3:30。）后上紧黄色齿轮的螺丝，防止后续脱落。然后开启最外侧这个缺口齿轮的螺丝，在保证压住黑色盖板的情况下先移除上面的金属覆盖层。接下来的操作可能无法复位，在没有信心的情况下请寻求专业师傅的帮助。

拆开最外侧这个齿轮上的黑色塑料板，可见内部的平板弹簧。

<div>
    <img class="postimg" src="/images/album/hassel/spring.jpeg" width="360px" />
    <div class="caption">500cx 外侧齿轮上的平板弹簧</div>
</div>

当然，看到这一幕是不容易的。更大可能性是，由于上次维修师傅留下的错误，这个弹簧并没有安装到位，所以在打开黑色盖板的一瞬间，这个平板弹簧就会飞出。上图作为一个参考，以防万一有人没能看到弹簧的初始位置。

# 机身复位

按照相反的流程我们可以比较轻松地将机身恢复，值得注意的是快门按钮对准以及反光板预升按钮的对准。经过我的尝试，反光板预升按钮似乎不能在安装过程中被正确对准，因此需要我们使用细螺丝刀等工具挑一下，具体可见参考视频[^4]的4:00处。此外，复位时需要注意左侧的OTF测光接口，可能需要镊子来固定其位置，以便两个小螺丝的安装。

# 参考样片

黑白胶片为修复前仅有的几张成功拍摄照片，彩色胶片为修复后拍摄的样片。

<div>
    <table class="borderlesstabel">
        <tr>
            <td>
                <img class="postimg" src="/images/album/hassel/bw1.jpeg" style="display:block; margin:0 auto; width: 360px;">
            </td>
            <td>
                <img class="postimg" src="/images/album/hassel/bw2.jpeg" style="display:block; margin:0 auto; width: 360px;">
            </td>
        </tr>
    </table>
    <div class="caption">Shek Kip Mei | FOMAPAN 200</div>
</div>

<div>
    <table class="borderlesstabel">
        <tr>
            <td>
                <img class="postimg" src="/images/album/hassel/c1.jpeg" style="display:block; margin:0 auto; width: 360px;">
            </td>
            <td>
                <img class="postimg" src="/images/album/hassel/c2.jpeg" style="display:block; margin:0 auto; width: 360px;">
            </td>
        </tr>
    </table>
    <div class="caption">CityUHK | Kodak Portra 400</div>
</div>

# 参考资料

[^1]: [Hasselblad Disassembly Part 1](https://www.youtube.com/watch?v=vOFdK7ySkj4)
[^2]: [Fix Old Cameras: Hasselblad Out of the Box](https://www.youtube.com/watch?v=rTLNoYaPwQ0)
[^3]: [Detailed explanation of the Hasselblad camera body](https://www.bilibili.com/video/BV1uw4m1f7x7)
[^4]: [Hasselblad 503CX repair](https://www.youtube.com/watch?v=ruf6xRCf-lU)

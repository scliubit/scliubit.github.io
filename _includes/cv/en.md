<header class="header"></header>

<article class="container">
    <section class="side" id="side">

        <!-- 左栏固定开关，记得及时删除这段代码 Start-->
        <!--
        <label class="switch" style="display: none;" onchange="switchFixed()">
            <script type="text/javaScript">
                    function switchFixed(){
                        var value = document.getElementById('side').style.position === 'fixed' ? 'absolute' : 'fixed';
                        document.getElementById('side').style.position = value;
                    }
                </script>
            <input id="cb" type="checkbox">
            <span class="slider round"></span>
        </label>
        <style>
            @media (min-width: 750px) {
                .switch {
                    position: relative;
                    display: inline-block !important;
                    width: 60px;
                    height: 34px;
                }

                .switch input {
                    display: none;
                }

                .slider {
                    position: absolute;
                    cursor: pointer;
                    top: 0;
                    left: 0;
                    right: 0;
                    bottom: 0;
                    background-color: #ccc;
                    -webkit-transition: .4s;
                    transition: .4s;
                }

                .slider:before {
                    position: absolute;
                    content: "";
                    height: 26px;
                    width: 26px;
                    left: 4px;
                    bottom: 4px;
                    background-color: white;
                    -webkit-transition: .4s;
                    transition: .4s;
                }

                input:checked+.slider {
                    background-color: #1abc9c;
                }

                input:focus+.slider {
                    box-shadow: 0 0 1px #1abc9c;
                }

                input:checked+.slider:before {
                    -webkit-transform: translateX(26px);
                    -ms-transform: translateX(26px);
                    transform: translateX(26px);
                }

                .slider.round {
                    border-radius: 34px;
                }

                .slider.round:before {
                    border-radius: 50%;
                }
            }
        </style>
        -->
        <!-- 左侧固定开关，记得及时删除这段代码 End-->

        <!-- 个人肖像 -->
        <section class="me">
            <section class="portrait">
                <!--
                <div class="loading">
                    <span></span>
                    <span></span>
                    <span></span>
                    <span></span>
                    <span></span>
                </div>-->
                <!-- 头像照片 -->
                <img class="avatar" src="assets/images/avatar.jpg" ><!--onload="loading()"-->
            </section>

            <h1 class="name">Anonymous</h1>
            <h4 class="info-job">硕士研究生在读 / 北京</h4>

        </section>

        <!-- 基本信息 -->
        <section class="profile info-unit">
            <h2>
                <i class="fa fa-user" aria-hidden="true"></i>基本信息
            </h2>
            <hr />
            <ul>
                <li>
                    <label>个人信息</label>
                    <span>Anonymous / 男 / 23岁</span>
                </li>
                <li>
                    <label>英语水平</label>
                    <span>CET-6</span>
                </li>
                <li>
                    <label>计算机水平</label>
                    <span>二级</span>
                </li>
            </ul>
        </section>

        <!-- 联系方式 -->
        <section class="contact info-unit">
            <h2>
                <i class="fa fa-phone" aria-hidden="true"></i>联系方式
            </h2>
            <hr />
            <ul>
                <li>
                    <label>手机</label>
                    <a href="tel:17610788560" target="_blank">176-1078-8560</a>
                </li>
                <li>
                    <label>邮箱</label>
                    <a href="mailto:scliubit@163.com" target="_blank">scliubit@163.com</a>
                </li>
                <li>
                    <label>个人主页</label>
                    <a href="https://scliubit.github.io/" target="_blank">scliubit.github.io</a>
                </li>
                <li>
                    <label>Github</label>
                    <a href="https://github.com/scliubit" target="_blank">github.com/scliubit</a>
                </li>
            </ul>
        </section>

        <!-- 技能点 -->
        <section class="skill info-unit">
            <h2>
                <i class="fa fa-code" aria-hidden="true"></i>技能点
            </h2>
            <hr />
            <ul>
                <li>
                    <label>吃</label>
                    <progress value="90" max="100"></progress>
                </li>
                <li>
                    <label>喝</label>
                    <progress value="85" max="100"></progress>
                </li>
                <li>
                    <label>睡</label>
                    <progress value="85" max="100"></progress>
                </li>
                <li>
                    <label>水群</label>
                    <progress value="85" max="100"></progress>
                </li>
                <li>
                    <label>刷论坛</label>
                    <progress value="70" max="100"></progress>
                </li>
                <li>
                    <label>打游戏</label>
                    <progress value="70" max="100"></progress>
                </li>
            </ul>
        </section>

        <section class="qrcode info-unit">
            <h2><i class="fa fa-qrcode" aria-hidden="true"></i>二维码 - 扫码立即施舍</h2>
            <hr />
            <img src="https://raw.githubusercontent.com/scliubit/scliubit.github.io/main/cv/assets/images/qr.jpg"
                style="width: 100%;" alt="">
        </section>

        <!-- 技术栈 -->
        <!-- <div class="stack info-unit">
                    <h2><i class="fa fa-code" aria-hidden="true"></i>其他</h2>
                    <hr/>
                    <ul>
                        <li>
                            <label>前端</label>
                            <span>React、jQuery、微信小程序、Bootstrap、SASS、LESS</span>
                        </li>
                        <li>
                            <label>后端</label>
                            <span>Node.js、MySQL、MongoDB、WordPress、ThinkPHP</span>
                        </li>
                        <li>
                            <label>其他</label>
                            <span>Git、SVN、Markdown</span>
                        </li>
                    </ul>
                </div> -->
    </section>

    <section class="main">

        <!-- 教育经历 -->
        <section class="edu info-unit">
            <h2>
                <i class="fa fa-graduation-cap" aria-hidden="true"></i>教育经历
            </h2>
            <hr />
            <ul>
                <li>
                    <h3>
                        <span>北京理工大学 - 电子信息工程专业（硕士在读）</span>
                        <time>2020.9-2023.7</time>
                    </h3>
                    <p>专业排名
                        <mark>-/500</mark>，目前还没有成果:)
                    </p>
                </li>
                <li>
                    <h3>
                        <span>北京理工大学 - 电子信息工程专业（本科）</span>
                        <time>2016.9-2020.7</time>
                    </h3>
                    <p>专业排名
                        <mark>7/96</mark>，成果基本上忘了XD
                    </p>
                </li>
            </ul>
        </section>

        <!-- 工作经历 -->
        <!--
        <section class="work info-unit">
            <h2>
                <i class="fa fa-shopping-bag" aria-hidden="true"></i>工作经历
            </h2>
            <hr />
            <ul>
                <li>
                    <h3>
                        <span>[经历1]XX公司－前端开发工程师（实习）</span>
                        <time>2016.X 至 2017.X</time>
                    </h3>
                    <ul class="info-content">
                        <li>深度参与XX项目迭代XX的前端开发工作，独立承担并完成XX、XX、XXXX等功能点的开发，主要维护并修复XX、XX、XX等功能点bug若干。项目采用技术栈
                            <mark>React+React Router+Node.js+SASS</mark>，实现
                            <mark>前后端完全分离</mark>。
                        </li>
                        <li>配合UI和后端，根据产品需求提供H5页面嵌入到后台模板，要求
                            <mark>移动端显示正常</mark>。
                        </li>
                        <li>主要参与XXXXXXX的静态页面开发工作，要求
                            <mark>在支付宝环境下完全兼容</mark>。
                        </li>
                    </ul>
                </li>
                <li>
                    <h3>
                        <span>[经历2]XX－前端开发工程师（实习）</span>
                        <time>20XX.10-20XX.7</time>
                    </h3>
                    <ul class="info-content">
                        <li>深度参与公司主线产品「XXXX」的前端开发工作，完成帖子快捷回复、
                            <mark>全站图片懒加载</mark>、活动banner、帖子管理（使用Yii框架）等功能。项目采用技术栈phpWind+NAMP。
                            <a href="http://itsay.tech/162/" target="_blank">
                                <i class="fa fa-link" aria-hidden="true"></i>博客文章</a>。
                        </li>
                        <li>主要参与公司产品「XXXX」的前端开发工作，实现接入微博、微信、QQ等
                            <mark>第三方账号登录</mark>等功能。项目采用技术栈WordPress+NAMP。
                        </li>
                        <li>活动页面的开发（七夕活动、抽奖活动以及承接外包页面）。</li>
                        <li>论坛
                            <mark>图片增量备份</mark>（CentOS+vsftpd+crontab）
                            <a href="#" target="_blank">
                                <i class="fa fa-link" aria-hidden="true"></i>博客文章</a>。
                        </li>
                    </ul>
                </li>
            </ul>
        </section>-->

        <!-- 项目经验 -->
        <!-- <section class="project info-unit">
            <h2>
                <i class="fa fa-terminal" aria-hidden="true"></i>个人项目
            </h2>
            <hr />
            <ul>
                <li>
                    <h3>
                        <span>[项目1]医学科学数据管理与共享平台</span>
                        <span class="link">
                            <a href="#" target="_blank">Demo</a>
                        </span>
                        <time>201X.X-201X.X</time>
                    </h3>
                    <ul class="info-content">
                        <li>技术栈：ThinkPHP+MongoDB+Axure</li>
                        <li>
                            <i class="fa fa-paper-plane-o" aria-hidden="true"></i>
                            [目标]实现多类型多来源医学科学数据的提交、管理和共享
                            <br />
                            <i class="fa fa-users" aria-hidden="true"></i>
                            [团队]同 2 位同专业同学一起
                            <br />
                            <i class="fa fa-bars" aria-hidden="true"></i>
                            [贡献]完成从
                            <mark>“调研-设计-实现-文档”</mark>等工作，主要负责系统原型、功能框架及数据提交流程、元数据及源数据的管理与共享方案的设计以及系统开发等工作
                            <br />
                            <i class="fa fa-thumbs-o-up" aria-hidden="true"></i>
                            [效果]作品最终取得第三届共享杯国家级竞赛“一等奖” （2/2000）
                        </li>
                    </ul>
                </li>
                <li>
                    <h3>
                        <span>[项目2]肿瘤流行病数据可视化</span>
                        <span class="link">
                            <a href="#" target="_blank">Demo</a>
                        </span>
                        <time>201X.X-201X.X</time>
                    </h3>
                    <ul class="info-content">
                        <li>技术栈：HTML 5+D3.js+ECharts+MySQL</li>
                        <li>
                            <i class="fa fa-paper-plane-o" aria-hidden="true"></i>
                            [目标]实现常见肿瘤流行病数据多维度可视化展示、数据透视及分析
                            <br />
                            <i class="fa fa-users" aria-hidden="true"></i>
                            [团队]与 1 位同学
                            <br />
                            <i class="fa fa-bars" aria-hidden="true"></i>
                            [贡献]分析项目需求，清洗并整理相关数据(扩展第三方知识组织系统和 Google trends 数据)，并用
                            <mark>D3.js</mark> 和
                            <mark>ECharts</mark> 进行图形化展示以及实现简易自动分析 功能
                            <br />
                            <i class="fa fa-thumbs-o-up" aria-hidden="true"></i>
                            [效果]作品取得第二届共享杯国家级竞赛“特等奖”(1/1500)
                        </li>
                    </ul>
                </li>
                <li>
                    <h3>
                        <span>[项目3]肿瘤流行病数据可视化</span>
                        <span class="link">
                            <a href="#" target="_blank">Demo</a>
                        </span>
                        <time>201X.X-201X.X</time>
                    </h3>
                    <ul class="info-content">
                        <li>技术栈：HTML 5+D3.js+ECharts+MySQL</li>
                        <li>
                            <i class="fa fa-paper-plane-o" aria-hidden="true"></i>
                            [目标]实现常见肿瘤流行病数据多维度可视化展示、数据透视及分析
                            <br />
                            <i class="fa fa-users" aria-hidden="true"></i>
                            [团队]与 1 位同学
                            <br />
                            <i class="fa fa-bars" aria-hidden="true"></i>
                            [贡献]分析项目需求，清洗并整理相关数据(扩展第三方知识组织系统和 Google trends 数据)，并用
                            <mark>D3.js</mark> 和
                            <mark>ECharts</mark> 进行图形化展示以及实现简易自动分析功能
                            <br />
                            <i class="fa fa-thumbs-o-up" aria-hidden="true"></i>
                            [效果]作品取得第二届共享杯国家级竞赛“特等奖”(1/1500)
                        </li>
                    </ul>
                </li>
                <li>
                    <h3>
                        <span>[项目4]肿瘤流行病数据可视化</span>
                        <span class="link">
                            <a href="#" target="_blank">Demo</a>
                        </span>
                        <time>201X.X-201X.X</time>
                    </h3>
                    <ul class="info-content">
                        <li>技术栈：HTML 5+D3.js+ECharts+MySQL</li>
                        <li>
                            <i class="fa fa-paper-plane-o" aria-hidden="true"></i>
                            [目标]实现常见肿瘤流行病数据多维度可视化展示、数据透视及分析
                            <br />
                            <i class="fa fa-users" aria-hidden="true"></i>
                            [团队]与 1 位
                            <br />
                            <i class="fa fa-bars" aria-hidden="true"></i>
                            [贡献]分析项目需求，清洗并整理相关数据(扩展第三方知识组织系统和 Google trends 数据)，并用
                            <mark>D3.js</mark> 和
                            <mark>ECharts</mark> 进行图形化展示以及实现简易自动分析 功能
                            <br />
                            <i class="fa fa-thumbs-o-up" aria-hidden="true"></i>
                            [效果]作品取得第二届共享杯国家级竞赛“特等奖”(1/1500)
                        </li>
                    </ul>
                </li>

            </ul>
        </section>
        -->

        <!-- 自我评价 -->
        <section class="work info-unit">
            <h2>
                <i class="fa fa-pencil" aria-hidden="true"></i>自我评价/期望
            </h2>
            <hr />
            <p>未来可期
            </p>
        </section>
    </section>
</article>



<footer class="footer">
    <p>© 2021 Anonymous. Last Modified
        <time>2021年03月14日</time>.
    </p>
</footer>

<!-- 侧栏 -->
<aside>
    <ul>
        <li>
            <a href="https://github.com/scliubit/scliubit.github.io" target="_blank">源代码</a>
        </li>
        <li>
            <a href="https://scliubit.github.io" target="_blank">Blog</a>
        </li>
    </ul>
</aside>

<script src="assets/js/index.js"></script>
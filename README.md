# PE/VC私募投融资 - 交易文件审阅

面向未上市公司股权融资的专业交易文件审阅能力：

- 适用于境内人民币架构，以及红筹/VIE 美元架构（尽管当前这类项目比例有所下降）；
- 支持公司/创始人方、投资人、领投/跟投及战略投资人等不同立场；
- 可审阅首轮整套文件初稿，跟踪后续多轮红线版本，并核验跨文件之间的冲突；
- 可输出完整的修改意见与建议、修订后版本、问题清单以及 Major Issue List（重大问题清单）等；
- 相较一般能力的突出优势在于：结合大量同类市场项目的统计数据，对于同一核心条款，不仅可提示市场主流做法与写法，还能提供不同做法的大致市场采用比例，并进一步给出相应的谈判建议。

机器识别名称为 `pe-vc-transaction-docs-review`。GitHub 仓库和安装包使用 `PE_VC_transaction_docs_review`，因为这些位置不能使用 `/`。

## 创建者与官方维护

- 创建者及官方维护者：Gardner's Vault
- 版权主体：Jiang Tao
- 官方仓库：[PE_VC_transaction_docs_review](https://github.com/hoangkiann-debug/PE_VC_transaction_docs_review)
- 问题反馈：[GitHub Issues](https://github.com/hoangkiann-debug/PE_VC_transaction_docs_review/issues)
- 公众号：加德纳的宝匣

官方版本以本仓库 GitHub Releases 及 [SkillHub 页面](https://skillhub.cn/skills/pe-vc-transaction-docs-review)发布的版本为准。每个版本均提供内容清单和 SHA-256 校验值，用于识别由 Gardner's Vault 发布和维护的正式版本。其他人可以依照 Apache License 2.0 使用和修改本项目，但修改版不应被表述为由 Gardner's Vault 官方维护或认可。

## 主要能力

- 覆盖人民币境内融资及境外美元直持/VIE架构；
- 支持公司/创始方、投资人、领投/跟投及战略投资人立场；
- 审阅增资协议、认购协议、股东协议、公司章程及相关配套文件；
- 追踪对方红线稿，识别新增、遗留、重开和已解决的问题；
- 检查定义、金额、股权、权利安排和争议解决的跨文件冲突；
- 对核心条款提示历史市场方向、不同方案的大致采用比例和谈判空间；
- 输出问题清单、完整修改条款、Word原生批注和 Major Issue List。

## 个性化使用

用户可以复制并填写 `skill/pe-vc-transaction-docs-review/assets/review-preferences-template.md`，把常用立场、条款底线、可接受的 Fallback、风险偏好和输出习惯固定下来。每次审阅时将偏好表与交易文件一并提供，Skill 会在不违背当前项目事实和法律核验要求的前提下优先采用。项目中的特殊让步不会自动变成长期偏好，除非用户明确确认。

## 持续维护

Gardner's Vault 将根据重要法律规则、市场实践及平台兼容性的变化持续更新法律依据、市场数据和审阅框架，并定期进行系统复核。每次正式发布均应更新版本记录、复核日期、内容清单和校验值，并通过公开发布测试、隐私扫描及一致性校验。具体规则见 [MAINTENANCE.md](MAINTENANCE.md) 和 [CHANGELOG.md](CHANGELOG.md)。

## 安装

### WorkBuddy

可以直接从 [SkillHub](https://skillhub.cn/skills/pe-vc-transaction-docs-review) 安装，也可以从 [GitHub Releases](https://github.com/hoangkiann-debug/PE_VC_transaction_docs_review/releases/latest) 下载最新的 WorkBuddy ZIP 安装包。

### Codex

将仓库中的 `skill/pe-vc-transaction-docs-review` 目录复制或链接到 Codex 的 Skills 目录，然后调用 `$pe-vc-transaction-docs-review`。

## 使用示例

```text
请使用 $pe-vc-transaction-docs-review，从投资人立场审阅这套 A 轮融资文件。先识别文件版本和相互冲突，再输出主要问题清单和逐条修改建议。
```

```text
请使用 $pe-vc-transaction-docs-review，比较本轮对方红线稿与上一版，区分新增风险、已解决事项和仍需谈判的重大问题。
```

## 适用边界

- 本 Skill 聚焦未上市公司 PE/VC 股权融资，不以已上市公司交易、私募基金设立备案、破产重整投资或单独的许可/BD 合同为主要场景；
- 本 Skill 提供专业审阅辅助，不构成法律意见，也不能替代承办律师结合具体项目作出的判断；
- 市场数据仅用于提供历史谈判背景，不是法律要求；法律法规、监管口径和市场实践可能变化，使用时应核验最新一手依据；
- 涉及中国法律相关事项，请咨询执业中国律师；涉及非中国法管辖事项，请咨询相应法域的执业律师。

## 许可与责任

本项目采用 Apache License 2.0。使用者应自行判断交易文件是否适合交由具体平台或连接器处理。创建者、版权及引用信息见 [AUTHORS.md](AUTHORS.md)、[NOTICE](NOTICE) 和 [CITATION.cff](CITATION.cff)；详细边界见 [DISCLAIMER.md](DISCLAIMER.md)、[PRIVACY.md](PRIVACY.md)、[SECURITY.md](SECURITY.md)；官方版本识别方式见 [OFFICIAL.md](OFFICIAL.md)，版本内容及文件校验值见 [release-manifest.json](release-manifest.json)。

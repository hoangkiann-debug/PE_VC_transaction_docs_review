# PE/VC私募交易文件审阅

面向**未上市公司股权融资**的开源交易文件审阅 Skill。它可以从公司/创始方或投资人立场出发，对人民币境内融资和境外美元融资文件进行结构化审阅，并生成律师可继续使用的审阅结果。

机器识别名称为 `pe-vc-transaction-docs-review`。GitHub 仓库和安装包使用 `PE_VC_transaction_docs_review`，因为这些位置不能使用 `/`。

## 主要能力

- 识别交易结构、文件版本、签约主体和整套文件之间的不一致；
- 审阅增资协议、认购协议、股东协议、公司章程及相关补充文件；
- 支持首轮全包审阅以及对方红线稿的后续轮次审阅；
- 输出问题清单、逐条批注计划、修改建议和 Major Issue List；
- 提供历史市场做法作为谈判背景，并提示需要核验的现行法律依据；
- 支持可回滚的 Word 原生批注工作流。

## 安装

### WorkBuddy

从 [GitHub Releases](https://github.com/hoangkiann-debug/PE_VC_transaction_docs_review/releases/latest) 下载 `PE_VC_transaction_docs_review-0.1.0-workbuddy.zip`，再通过 WorkBuddy 的本地 Skill 导入功能上传。压缩包内只有一个顶层目录：`pe-vc-transaction-docs-review`。

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
- 非中国法管辖事项应由相应法域的合资格律师确认。

## 隐私与开源

公开版本采用明确的文件白名单生成，不包含客户文件、客户或交易参与方名称、私有文章原文、内部案例材料、本地路径或底层来源登记表。用户仍应自行判断其交易文件是否适合交由具体平台或连接器处理。

本项目采用 Apache License 2.0。详细边界见 [DISCLAIMER.md](DISCLAIMER.md)、[PRIVACY.md](PRIVACY.md)、[SECURITY.md](SECURITY.md)；版本内容及文件校验值见 [release-manifest.json](release-manifest.json)。

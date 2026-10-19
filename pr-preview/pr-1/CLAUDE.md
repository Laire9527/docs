# document_manager

團隊內部一起 review 的整理文件，以 GitHub Pages 發佈（`main` 分支、根目錄）。文件依專案分資料夾，每份文件是一個獨立的 `.html`。

## 結構

```
index.html                  首頁：專案目錄（只放專案卡片，不放文件）
<Project>/<project>.html    專案頁：該專案的文件目錄（依分類列出文件）
<Project>/<文件>.html        文件本身
```

目前專案（首頁順序）：

| 顯示名稱 | 資料夾 | 專案頁 |
| --- | --- | --- |
| Vigil Cambox | `Vigil_Cambox/` | `vigil_cambox.html` |
| FPGA Board | `FPGA_Board/` | `fpga_board.html` |
| Trim+ | `Trim_plus/` | `trim_plus.html` |
| Forge | `Forge/` | `forge.html` |

- 資料夾、檔名、路徑不要用 `+`、空白等特殊符號（例如 Trim+ 一律寫成 `Trim_plus`）；頁面上顯示的名稱照原名。
- GitHub Pages 網址區分大小寫，連結要跟資料夾名稱大小寫完全一致。
- 新專案：開資料夾、放一個專案頁（複製現有空專案頁的版面），首頁加一張卡片。
- 空專案：專案頁與首頁卡片都顯示「尚無文件」，卡片仍可點進專案頁。

文件內容與溝通一律使用繁體中文。目標是「室內一起看、看得清楚」，不需要做到太精緻。

## Git 流程

- 在 `develop` 分支上修改與 commit；使用者確認後自己合併到 `main`。
- 不要直接 commit 到 `main`，也不要 push，除非使用者明確要求。
- 改完檔案先回報，等使用者說要 commit 再 commit。

## 新增文件頁面的規範

### 1. 文件本身

- 單一自含的 HTML 檔，CSS 寫在 `<style>` 內，不依賴外部 JS（Google Fonts 可以）。
- 放在所屬專案的資料夾內，跟專案頁同一層。
- `<title>` 寫清楚，專案頁卡片標題直接沿用它。
- 樣式可以每份文件不同，但要深色或支援深色模式，背景不要刺眼。
- 窄螢幕（手機）也要能讀：表格放進可橫向捲動的容器，不要讓整頁橫向捲動。

### 2. 必備導覽按鈕

每份文件都要有這兩個連結，樣式跟隨該文件自己的風格：

- **「▲ 回到最上方」**：`href="#top"`，並在標題區（header 或 h1）加上 `id="top"`。
- **「← 回上一頁」**：`href="<project>.html"`（連到同資料夾的專案頁，不用 `history.back()`，這樣直接開網址也能回去）。

位置依文件版面而定，目前 `FPGA_Board/` 三份的做法可當參考：

| 版面 | 放法 | 範例 |
| --- | --- | --- |
| 左側 sticky 目錄 | 目錄最下方，用分隔線隔開，兩個連結樣式同目錄項目 | `RacerTechXCYP_USB2MIPI_handover_report.html` |
| 左側浮動目錄卡片 | 卡片內「回到最上方」實心按鈕，下方「回上一頁」外框按鈕 | `innolux_lcd_3bits_to_6bits.html` |
| 頂端 sticky 目次列 | 目次列多切一行，第一行放兩顆按鈕，第二行放原本目次 | `powerboard_handover_toCYP.html` |

注意：
- 側邊目錄若在窄螢幕會隱藏，按鈕也會跟著消失，要提醒使用者或另外處理。
- 頂端 sticky 列變高時，記得調整 `section` 的 `scroll-margin-top`，避免跳轉後標題被蓋住。

### 3. 更新專案頁

- 在專案頁（`<Project>/<project>.html`）對應分類的 `<ul>` 內加一段：

  ```html
  <li>
    <a class="doc" href="檔名.html">
      <span class="title">（沿用文件的 &lt;title&gt;）</span>
      <span class="desc">一句話說明：主題＋主要章節重點。</span>
    </a>
  </li>
  ```

- 沒有合適分類時，新增一組 `<h2>分類名</h2>` + `<ul>`，並向使用者確認分類名稱。
- 新文件加在該分類最後；順序使用者會自己調，不用另訂規則。
- `.desc` 是根據章節標題摘要的，回報時告知使用者可自行修改。
- 專案頁原本是「尚無文件」時：把 `<p class="empty">` 換成分類 `<h2>` + `<ul>`（寫法同 `FPGA_Board/fpga_board.html`）。
- 同時更新首頁 `index.html` 該專案卡片的 `.desc`（分類＋文件數，例如「FPGA / 光引擎板、LCD 面板 · 3 份文件」）。
- `class="comment"` 的元素在頁面上是隱藏的（給維護者看的註解），不要刪掉也不要改成顯示。

## 回報時

- 說明改了哪些檔案、放在哪裡、沿用了什麼樣式。
- 沒有用瀏覽器實際打開確認時，要明說。

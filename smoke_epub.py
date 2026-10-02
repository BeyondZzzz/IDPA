"""Generate a small EPUB to verify the local packaging environment."""

from pathlib import Path

from ebooklib import epub


def main() -> None:
    out = Path(__file__).resolve().parent / "runs" / "smoke.epub"
    out.parent.mkdir(parents=True, exist_ok=True)

    book = epub.EpubBook()
    book.set_identifier("docflow-smoke-v1")
    book.set_title("DocFlow 环境测试")
    book.set_language("zh-CN")

    chapter = epub.EpubHtml(
        title="测试章节", file_name="chapter.xhtml", lang="zh-CN"
    )
    chapter.content = "<h1>测试章节</h1><p>原文：金额 100 元。</p>"
    book.add_item(chapter)
    book.toc = (epub.Link("chapter.xhtml", "测试章节", "ch1"),)
    book.spine = ["nav", chapter]
    book.add_item(epub.EpubNav())
    book.add_item(epub.EpubNcx())

    epub.write_epub(str(out), book, {"raise_exceptions": True})
    if not out.is_file() or out.stat().st_size == 0:
        raise RuntimeError("EPUB output is missing or empty")
    print(f"Generated: {out}")


if __name__ == "__main__":
    main()

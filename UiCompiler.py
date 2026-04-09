from PySide6.scripts.pyside_tool import qt_tool_wrapper

qt_tool_wrapper("uic", ["-g", "python", "layout.ui", "-o", "ui_layout.py"])

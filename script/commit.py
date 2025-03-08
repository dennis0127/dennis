#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess
import os


def commit(msg: str):
    current_path = os.getcwd()
    subprocess.run(["git", "add", "."], cwd=current_path)
    subprocess.run(["git", "commit", "-m", msg], cwd=current_path)
    subprocess.run(["git", "push"], cwd=current_path)


if __name__ == "__main__":
    msg = input("请输入提交信息:")
    commit(msg)

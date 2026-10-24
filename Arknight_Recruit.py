import random
import time
from itertools import combinations

STAR_1 = {
    "Lancet-2": ("YL", "FA", "ZL"),
    "Castle-3": ("JW", "CL", "ZY"),
    "THRM-EX": ("TZ", "CL", "BF"),
    "正义骑士号": ("JJ", "FA", "ZY"),
    "Friston-3": ("ZZ", "CL", "FH"),
    "PhonoR-0": ("FZ", "FA", "YS"),
    "CONFESS-47": ("XF", "CL", "KC"),
    "GALLUS²": ("SS", "FA", "XR"),
}
STAR_2 = {
    "夜刀": ("XF", "CL"),
    "黑角": ("ZZ", "CL"),
    "巡林者": ("JJ", "FA"),
    "杜林": ("SS", "FA"),
    "12F": ("SS", "FA"),
}
STAR_3 = {
    "芬": ("XF", "CL", "HF"),
    "翎羽": ("XF", "CL", "AT", "HF"),
    "香草": ("XF", "CL", "HF"),
    "玫兰莎": ("JW", "CL", "AT", "SC"),
    "泡普卡": ("JW", "CL", "QG", "SC"),
    "月见夜": ("JW", "CL", "AT"),
    "米格鲁": ("ZZ", "CL", "FH"),
    "斑点": ("ZZ", "CL", "FH", "ZL"),
    "克洛丝": ("JJ", "FA", "AT"),
    "安德切尔": ("JJ", "FA", "AT"),
    "空爆": ("JJ", "FA", "QG"),
    "炎熔": ("SS", "FA", "QG"),
    "史都华德": ("SS", "FA", "AT"),
    "芙蓉": ("YL", "FA", "ZL"),
    "安赛尔": ("YL", "FA", "ZL"),
    "梓兰": ("FZ", "FA", "JS"),
}
STAR_4 = {
    "安比尔": ("JJ", "FA", "AT", "JS"),
    "梅": ("JJ", "FA", "AT", "JS"),
    "红云": ("JJ", "FA", "AT"),
    "白雪": ("JJ", "FA", "QG", "JS"),
    "流星": ("JJ", "FA", "AT", "XR"),
    "杰西卡": ("JJ", "FA", "AT", "SC"),
    "酸糖": ("JJ", "FA", "AT"),
    "松果": ("JJ", "FA", "QG", "AT"),
    "猎蜂": ("JW", "CL", "AT"),
    "慕斯": ("JW", "CL", "AT"),
    "霜叶": ("JW", "CL", "JS", "AT"),
    "缠丸": ("JW", "CL", "AT", "SC"),
    "杜宾": ("JW", "CL", "AT", "ZY"),
    "艾丝黛尔": ("JW", "CL", "QG", "SC"),
    "宴": ("JW", "CL", "AT", "SC"),
    "刻刀": ("JW", "CL", "BF", "AT"),
    "芳汀": ("JW", "CL", "AT"),
    "杰克": ("JW", "CL", "AT"),
    "古米": ("ZZ", "CL", "FH", "ZL"),
    "蛇屠箱": ("ZZ", "CL", "FH"),
    "角峰": ("ZZ", "CL", "FH"),
    "泡泡": ("ZZ", "CL", "FH"),
    "苏苏洛": ("YL", "FA", "ZL"),
    "调香师": ("YL", "FA", "ZL"),
    "末药": ("YL", "FA", "ZL"),
    "清流": ("YL", "FA", "ZL", "ZY"),
    "地灵": ("FZ", "FA", "JS"),
    "波登可": ("FZ", "FA", "JS", "ZL"),
    "格雷伊": ("SS", "FA", "QG", "JS"),
    "远山": ("SS", "FA", "QG"),
    "夜烟": ("SS", "FA", "AT", "XR"),
    "卡达": ("SS", "FA", "AT", "KC"),
    "深靛": ("SS", "FA", "AT", "KC"),
    "阿消": ("TZ", "CL", "WY"),
    "暗索": ("TZ", "CL", "WY"),
    "砾": ("TZ", "CL", "KH", "FH"),
    "孑": ("TZ", "CL", "KH", "AT"),
    "桃金娘": ("XF", "CL", "HF", "ZL"),
    "红豆": ("XF", "CL", "AT", "HF"),
    "清道夫": ("XF", "CL", "AT", "HF"),
    "豆苗": ("XF", "FA", "HF", "ZH"),
    "罗比菈塔": ("FZ", "CL", "FH", "ZY"),
}
STAR_5 = {
    "幽灵鲨": ("JW", "CL", "QG", "SC"),
    "布洛卡": ("JW", "CL", "QG", "SC"),
    "星极": ("JW", "CL", "AT", "FH"),
    "诗怀雅": ("JW", "CL", "AT", "ZY"),
    "因陀罗": ("JW", "CL", "AT", "SC"),
    "断崖": ("JW", "CL", "AT", "QG"),
    "燧石": ("JW", "CL", "AT"),
    "赤冬": ("JW", "CL", "AT", "SC"),
    "羽毛笔": ("JW", "CL", "AT"),
    "蓝毒": ("JJ", "FA", "AT"),
    "灰喉": ("JJ", "FA", "AT"),
    "送葬人": ("JJ", "FA", "QG"),
    "守林人": ("JJ", "FA", "AT", "BF"),
    "普罗旺斯": ("JJ", "FA", "AT"),
    "陨星": ("JJ", "FA", "QG", "XR"),
    "白金": ("JJ", "FA", "AT"),
    "慑砂": ("JJ", "FA", "QG", "XR"),
    "安哲拉": ("JJ", "FA", "JS", "AT"),
    "四月": ("JJ", "FA", "AT"),
    "奥斯塔": ("JJ", "FA", "QG"),
    "熔泉": ("JJ", "FA", "AT"),
    "吽": ("ZZ", "CL", "FH", "ZL"),
    "火神": ("ZZ", "CL", "SC", "FH", "AT"),
    "可颂": ("ZZ", "CL", "FH", "WY"),
    "雷蛇": ("ZZ", "CL", "FH", "AT"),
    "临光": ("ZZ", "CL", "FH", "ZL"),
    "石棉": ("ZZ", "CL", "FH", "AT"),
    "赫默": ("YL", "FA", "ZL"),
    "白面鸮": ("YL", "FA", "ZL", "ZY"),
    "华法琳": ("YL", "FA", "ZL", "ZY"),
    "絮雨": ("YL", "FA", "ZL"),
    "格劳克斯": ("FZ", "FA", "JS", "KC"),
    "真理": ("FZ", "FA", "JS", "AT"),
    "初雪": ("FZ", "FA", "XR"),
    "梅尔": ("FZ", "FA", "ZH", "KC"),
    "巫恋": ("FZ", "FA", "XR"),
    "月禾": ("FZ", "FA", "ZY", "SC"),
    "夜魔": ("SS", "FA", "AT", "ZL", "JS"),
    "惊蛰": ("SS", "FA", "AT"),
    "莱恩哈特": ("SS", "FA", "QG", "BF"),
    "蜜蜡": ("SS", "FA", "QG", "FH"),
    "爱丽丝": ("SS", "FA", "AT"),
    "狮蝎": ("TZ", "CL", "AT", "SC"),
    "食铁兽": ("TZ", "CL", "WY", "JS"),
    "槐琥": ("TZ", "CL", "KH", "XR"),
    "红": ("TZ", "CL", "KH", "KC"),
    "崖心": ("TZ", "CL", "WY", "AT"),
    "卡夫卡": ("TZ", "CL", "KH", "KC"),
    "乌有": ("TZ", "CL", "KH", "AT"),
    "绮良": ("TZ", "CL", "AT", "SC"),
    "德克萨斯": ("XF", "CL", "HF", "KC"),
    "苇草": ("XF", "CL", "HF", "AT"),
    "凛冬": ("XF", "CL", "HF", "ZY"),
    "极境": ("XF", "CL", "HF", "ZY"),
    "贾维": ("XF", "CL", "HF", "AT"),
    "桑葚": ("YL", "FA", "ZL"),
}
STAR_6 = {
    "银灰": ("JW", "CL", "AT", "ZY"),
    "陈": ("JW", "CL", "BF", "AT"),
    "煌": ("JW", "CL", "AT", "SC"),
    "赫拉格": ("JW", "CL", "AT", "SC"),
    "斯卡蒂": ("JW", "CL", "AT", "SC"),
    "棘刺": ("JW", "CL", "AT", "FH"),
    "史尔特尔": ("JW", "CL", "AT"),
    "山": ("JW", "CL", "AT", "SC"),
    "帕拉斯": ("JW", "CL", "AT", "ZY"),
    "能天使": ("JJ", "FA", "AT"),
    "黑": ("JJ", "FA", "AT"),
    "早露": ("JJ", "FA", "AT", "KC"),
    "空弦": ("JJ", "FA", "AT"),
    "星熊": ("ZZ", "CL", "FH", "AT"),
    "塞雷娅": ("ZZ", "CL", "FH", "ZL", "ZY"),
    "森蚺": ("ZZ", "CL", "AT", "SC", "FH"),
    "瑕光": ("ZZ", "CL", "AT", "FH", "ZL"),
    "泥岩": ("ZZ", "CL", "AT", "SC", "FH"),
    "夜莺": ("YL", "FA", "ZL", "ZY"),
    "闪灵": ("YL", "FA", "ZL", "ZY"),
    "凯尔希": ("YL", "FA", "ZH", "ZL"),
    "麦哲伦": ("FZ", "FA", "AT", "ZY", "JS"),
    "铃兰": ("FZ", "FA", "AT", "ZY", "JS"),
    "莫斯提马": ("SS", "FA", "QG", "ZY", "KC"),
    "伊芙利特": ("SS", "FA", "QG", "XR"),
    "刻俄柏": ("SS", "FA", "AT", "KC"),
    "异客": ("SS", "FA", "AT"),
    "卡涅利安": ("SS", "FA", "QG", "FH"),
    "阿": ("TZ", "FA", "ZY", "AT"),
    "傀影": ("TZ", "CL", "KH", "KC", "AT"),
    "温蒂": ("TZ", "CL", "AT", "WY", "KC"),
    "水月": ("TZ", "CL", "KC", "AT"),
    "推进之王": ("XF", "CL", "HF", "AT"),
    "风笛": ("XF", "CL", "HF", "AT"),
    "嵯峨": ("XF", "CL", "HF", "AT"),
    "琴柳": ("XF", "CL", "HF", "ZY"),
}

STAR_6_NEW_YEAR_LIMITED = {
    "年": ("ZZ", "CL", "FH", "ZY"),
    "夕": ("SS", "FA", "QG", "AT", "KC"),
    "令": ("FZ", "FA", "ZH", "ZY", "KC"),
    "重岳": ("JW", "CL", "BF"),
    "黍": ("ZZ", "CL", "FH", "ZL", "ZY"),
    "余": (""),
}
STAR_6_ANNIVERSARY_LIMITED = {
    "赫拉格": ("JW", "CL", "AT", "SC"),
}
STAR_6_SUMMER_LIMITED = {
    "赫拉格": ("JW", "CL", "AT", "SC"),
}
STAR_6_HALF_ANNIVERSARY_LIMITED = {
    "赫拉格": ("JW", "CL", "AT", "SC"),
}

FIXED_STAR_TAG = ("6S", "5S", "2S", "1S")

TRANSLATOR = {
    "6S": "高级资深干员",
    "5S": "资深干员",
    "2S": "新手",
    "1S": "支援机械",
    "XF": "先锋干员",
    "JW": "近卫干员",
    "ZZ": "重装干员",
    "JJ": "狙击干员",
    "SS": "术师干员",
    "YL": "医疗干员",
    "FZ": "辅助干员",
    "TZ": "特种干员",
    "CL": "近战位",
    "FA": "远程位",
    "KC": "控场",
    "BF": "爆发",
    "ZL": "治疗",
    "ZY": "支援",
    "HF": "费用回复",
    "AT": "输出",
    "SC": "生存",
    "QG": "群攻",
    "FH": "防护",
    "JS": "减速",
    "XR": "削弱",
    "KH": "快速复活",
    "WY": "位移",
    "ZH": "召唤",
    "YS": "元素",
    "GK": "高空",
}

ALL_CHARS = (STAR_1, STAR_2, STAR_3, STAR_4, STAR_5)

ALL_CHARS_WITH_6S = (STAR_1, STAR_2, STAR_3, STAR_4, STAR_5, STAR_6)

CHAR_TO_STAR = {}
for _sd, _sl in [
    (STAR_1, 1),
    (STAR_2, 2),
    (STAR_3, 3),
    (STAR_4, 4),
    (STAR_5, 5),
    (STAR_6, 6),
]:
    for _char in _sd:
        CHAR_TO_STAR[_char] = _sl

ALL_NORMAL_TAGS = [tag for tag in TRANSLATOR if tag not in FIXED_STAR_TAG]
SPECIAL_STAR_TAGS = ("1S", "5S", "6S")

NOTE_TS = 1793484000  # 2026-11-01 06:00
UPDATE_DURATION = 21600  # 6小时
NOTE_CHAR = {"琴柳": 6, "桑葚": 5, "罗比菈塔": 4}
NOTE_TIME_STR = time.strftime("%Y-%m-%d %H:%M", time.localtime(NOTE_TS)) + '-' + time.strftime("%H:%M", time.localtime(NOTE_TS + UPDATE_DURATION))


def find_all_special_combinations() -> dict:
    """查询所有标签中能组成特殊组合(只出1/4/5/6星)的全部组合"""
    result = {}
    all_tags = list(ALL_NORMAL_TAGS) + list(SPECIAL_STAR_TAGS)
    for r in range(1, 4):
        for combo in combinations(all_tags, r):
            match_chars = find_match_char(list(combo))
            if not match_chars:
                continue
            star_set = set()
            has_star_3 = False
            for char in match_chars:
                star = CHAR_TO_STAR.get(char, 0)
                star_set.add(star)
                if star == 3:
                    has_star_3 = True
                    break
            if has_star_3:
                continue
            if star_set & {4, 5, 6} or star_set == {1}:
                result[combo] = match_chars
    return result


def string_process(original_str: str) -> set:
    return list(set(original_str.upper().split(" ")))


def cap(list1: list, list2: list) -> list:
    set2 = set(list2)
    return [x for x in list1 if x in set2]


def find_match_char(tag_list: list) -> list:
    result = []
    if len(tag_list) == 0:
        for cdict in ALL_CHARS:
            result += list(cdict.keys())
        return result
    if len(tag_list) > 3:
        return []
    fixed_star_in_tags = [tag for tag in FIXED_STAR_TAG if tag in tag_list]
    if len(fixed_star_in_tags) > 1:
        return []
    if "1S" in tag_list:
        find_list = [STAR_1]
    elif "2S" in tag_list:
        find_list = [STAR_2]
    elif "5S" in tag_list:
        find_list = [STAR_5]
    elif "6S" in tag_list:
        find_list = [STAR_6]
    else:
        find_list = list(ALL_CHARS)
    for tag in FIXED_STAR_TAG:
        if tag in tag_list:
            tag_list.remove(tag)
    for chardict in find_list:
        for char in chardict:
            is_char_to_find = True
            for tag in tag_list:
                if tag not in chardict[char]:
                    is_char_to_find = False
                    break
            if is_char_to_find:
                result.append(char)
    return result


def all_subsets(lst):
    subsets = []
    for r in range(1, len(lst) + 1 if len(lst) < 4 else 4):
        subsets.extend(combinations(lst, r))
    return subsets


def find_all_match_char(tag_list: list) -> list:
    result = dict()
    subsets_of_list = all_subsets(tag_list)
    for combination in subsets_of_list:
        current_combination = find_match_char(list(combination))
        if len(current_combination) > 0:
            result[combination] = current_combination
    return result


def check_all_tags_accuracy(char_dict_list: list = ALL_CHARS_WITH_6S) -> None:
    accuracy = True
    for dict in char_dict_list:
        for char in dict:
            for tag in dict[char]:
                if tag not in TRANSLATOR:
                    accuracy = False
                    print(f"标签缩写 {tag} 不存在，请检查后重新输入。")
    if accuracy:
        print("所有标签缩写均正确。")
    return


def find_combinations_can_get_1s_4s_5s_6s(tag_list: list) -> dict:
    result = dict()
    all_match = find_all_match_char(tag_list)
    for combination, match_chars in all_match.items():
        star_set = set()
        has_star_3 = False
        for char in match_chars:
            star = CHAR_TO_STAR.get(char, 0)
            star_set.add(star)
            if star == 3:
                has_star_3 = True
                break
        if has_star_3:
            continue
        if star_set & {4, 5, 6}:
            result[combination] = match_chars
        elif star_set == {1}:
            result[combination] = match_chars
    return result


def get_update_note():
    if time.time() >= NOTE_TS:
        return ""
    ansi_colors = {6: "31", 5: "33", 4: "35", 3: "34", 2: "32", 1: "90"}
    note_char_list = list(NOTE_CHAR)
    for i, char in enumerate(note_char_list):
        star = NOTE_CHAR[char]
        note_char_list[i] = f"\033[{ansi_colors[star]}m{char}\033[0m"
    return f"\n注：干员 {' ,  '.join(note_char_list)} 将在 {NOTE_TIME_STR} 更新后加入公开招募，目前不可招募！"


def main() -> None:
    ansi_colors = {6: "31", 5: "33", 4: "35", 3: "34", 2: "32", 1: "90"}

    def color_chars(chars):
        return ", ".join(
            f"\033[{ansi_colors.get(CHAR_TO_STAR.get(c, 0), '0')}m{c}\033[0m"
            for c in chars
        )

    def print_special_combos(combos_dict, title):
        print(f"\n{title}:")
        if combos_dict:
            for combo, chars in combos_dict.items():
                tag_str = " + ".join(f"{t}({TRANSLATOR.get(t, t)})" for t in combo)
                print(f"  {tag_str} \u2192 {color_chars(chars)}")
        else:
            print("  无")

    while True:
        text = input("输入标签缩写（输入exit退出，输入all查询全局特殊组合）->")
        if text.lower() == "exit":
            break
        if text.lower() == "all":
            print("\n正在查询全局特殊组合，请稍候...")
            all_special = find_all_special_combinations()
            print_special_combos(all_special, "全局特殊组合列表")
            note = get_update_note()
            if note:
                print(note)
            print()
            continue
        tag_list = string_process(text) if len(text) > 0 else []
        if not tag_list:
            continue
        print(
            "标签翻译:",
            "  ".join(f"{tag}:{TRANSLATOR.get(tag, '?')}" for tag in tag_list),
        )

        all_match = find_all_match_char(tag_list)
        print("\n所有匹配组合:")
        if all_match:
            for combo, chars in all_match.items():
                tag_str = " + ".join(f"{t}({TRANSLATOR.get(t, t)})" for t in combo)
                print(f"  {tag_str} \u2192 {color_chars(chars)}")
        else:
            print("  无")

        special = find_combinations_can_get_1s_4s_5s_6s(tag_list)
        print_special_combos(special, "可出1/4/5/6星组合")
        note = get_update_note()
        if note:
            print(note)
        print()


def gui() -> None:
    import tkinter as tk
    from tkinter import scrolledtext

    root = tk.Tk()
    root.title("明日方舟公招缩写速查")
    root.geometry("900x700")

    star_colors = {6: "red", 5: "orange", 4: "purple", 3: "blue", 2: "green", 1: "gray"}

    def insert_with_color(text_widget, chars):
        for i, char in enumerate(chars):
            star = CHAR_TO_STAR.get(char, 0)
            tag = f"c{star}"
            text_widget.insert(tk.END, char, tag)
            if i < len(chars) - 1:
                text_widget.insert(tk.END, ", ")

    input_frame = tk.Frame(root)
    input_frame.pack(fill=tk.X, padx=10, pady=(10, 5))

    tk.Label(input_frame, text="输入标签（空格分隔）:").pack(side=tk.LEFT)
    entry = tk.Entry(input_frame, width=40)
    entry.pack(side=tk.LEFT, padx=5)

    def search():
        all_text.config(state="normal")
        special_text.config(state="normal")
        tag_label.config(text="")
        all_text.delete(1.0, tk.END)
        special_text.delete(1.0, tk.END)

        text = entry.get().strip()
        if not text:
            return
        tag_list = string_process(text)
        if not tag_list:
            return

        translations = "  ".join(
            f"{tag}:{TRANSLATOR.get(tag, '?')}" for tag in tag_list
        )
        tag_label.config(text=translations)

        all_match = find_all_match_char(tag_list)
        all_text.insert(tk.END, "所有匹配组合:\n")
        if all_match:
            for combo, chars in all_match.items():
                tag_str = " + ".join(f"{t}({TRANSLATOR.get(t, t)})" for t in combo)
                all_text.insert(tk.END, f"{tag_str} \u2192 ")
                insert_with_color(all_text, chars)
                all_text.insert(tk.END, "\n")
        else:
            all_text.insert(tk.END, "无\n")

        special = find_combinations_can_get_1s_4s_5s_6s(tag_list)
        special_text.insert(tk.END, "可出1/4/5/6星组合:\n")
        if special:
            for combo, chars in special.items():
                tag_str = " + ".join(f"{t}({TRANSLATOR.get(t, t)})" for t in combo)
                special_text.insert(tk.END, f"{tag_str} \u2192 ")
                insert_with_color(special_text, chars)
                special_text.insert(tk.END, "\n")
        else:
            special_text.insert(tk.END, "无\n")
        if time.time() < NOTE_TS:
            note = "注：干员 "
            all_text.insert(tk.END, f"\n{note}")
            for char in NOTE_CHAR:
                star = NOTE_CHAR[char]
                all_text.insert(tk.END, char, f"c{star}")
                if char != list(NOTE_CHAR.keys())[-1]:
                    all_text.insert(tk.END, " ,  ")
            all_text.insert(
                tk.END, f" 将在 {NOTE_TIME_STR} 更新后加入公开招募，目前不可招募！"
            )
            special_text.insert(tk.END, f"\n{note}")
            for char in NOTE_CHAR:
                star = NOTE_CHAR[char]
                special_text.insert(tk.END, char, f"c{star}")
                if char != list(NOTE_CHAR.keys())[-1]:
                    special_text.insert(tk.END, " ,  ")
            special_text.insert(
                tk.END, f" 将在 {NOTE_TIME_STR} 更新后加入公开招募，目前不可招募！"
            )
        all_text.config(state="disabled")
        special_text.config(state="disabled")

    def search_all():
        top = tk.Toplevel(root)
        top.title("全局特殊组合列表")
        top.geometry("800x600")
        text_area = scrolledtext.ScrolledText(top, wrap=tk.WORD)
        for star, color in star_colors.items():
            text_area.tag_config(f"c{star}", foreground=color)
        text_area.pack(fill=tk.BOTH, expand=True)
        text_area.insert(tk.END, "正在查询全局特殊组合，请稍候...\n")
        text_area.config(state="disabled")
        top.update()

        def do_search():
            text_area.config(state="normal")
            text_area.delete(1.0, tk.END)
            all_special = find_all_special_combinations()
            if time.time() < NOTE_TS:
                text_area.insert(tk.END, "注：干员 ")
                for char in NOTE_CHAR:
                    star = NOTE_CHAR[char]
                    text_area.insert(tk.END, char, f"c{star}")
                    if char != list(NOTE_CHAR.keys())[-1]:
                        text_area.insert(tk.END, " ,  ")
                text_area.insert(
                    tk.END,
                    f" 将在 {NOTE_TIME_STR} 更新后加入公开招募，目前不可招募！\n\n",
                )
            if all_special:
                for combo, chars in all_special.items():
                    tag_str = " + ".join(f"{t}({TRANSLATOR.get(t, t)})" for t in combo)
                    text_area.insert(tk.END, f"{tag_str} \u2192 ")
                    insert_with_color(text_area, chars)
                    text_area.insert(tk.END, "\n")
            else:
                text_area.insert(tk.END, "无\n")
            text_area.config(state="disabled")

        top.after(100, do_search)

    btn = tk.Button(input_frame, text="查询", command=search, width=8)
    btn.pack(side=tk.LEFT)
    btn_all = tk.Button(input_frame, text="全局特殊组合", command=search_all, width=12)
    btn_all.pack(side=tk.LEFT, padx=5)

    entry.bind("<Return>", lambda e: search())

    tag_label = tk.Label(root, text="", wraplength=860, justify=tk.LEFT, fg="blue")
    tag_label.pack(fill=tk.X, padx=10, pady=5)

    all_frame = tk.LabelFrame(root, text="所有匹配组合")
    all_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
    all_text = scrolledtext.ScrolledText(all_frame, wrap=tk.WORD)
    for star, color in star_colors.items():
        all_text.tag_config(f"c{star}", foreground=color)
    all_text.pack(fill=tk.BOTH, expand=True)
    all_text.config(state="disabled")

    special_frame = tk.LabelFrame(root, text="可出1/4/5/6星组合（无3星）")
    special_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))
    special_text = scrolledtext.ScrolledText(special_frame, wrap=tk.WORD)
    for star, color in star_colors.items():
        special_text.tag_config(f"c{star}", foreground=color)
    special_text.pack(fill=tk.BOTH, expand=True)
    special_text.config(state="disabled")

    root.mainloop()


if __name__ == "__main__":
    mode = input("选择模式: 1.命令行模式  其他.GUI模式 (输入): ")
    if mode == "1":
        main()
    else:
        try:
            gui()
        except Exception:
            print("GUI模式不可用，切换到命令行模式。")
            main()

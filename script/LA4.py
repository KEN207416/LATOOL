import re

def filter_and_convert(input_path, output_path):
    try:
        # 读取输入文件
        with open(input_path, 'r') as file:
            lines = file.readlines()

        # 过滤符号并转换内容
        converted_lines = []
        for line in lines:
            # 使用正则表达式匹配数字
            numbers = re.findall(r'\d+', line)
            if len(numbers) == 2:
                # 转换为"数字 两个空格 数字"格式，并添加到列表中
                converted_lines.append(f"{numbers[0]}  {numbers[1]}")

        # 将转换后的内容写入输出文件
        with open(output_path, 'w') as output_file:
            output_file.write('\n'.join(converted_lines))

        print("转换成功")
    except Exception as e:
        print("转换失败:", str(e))

def main():
    # 提示用户输入文件路径
    input_path = input("请输入py配置文件路径: ")
    output_path = '/storage/emulated/0/Download/蓝桉/美化配置/输出/PY转换TXT配置输出.txt'
    filter_and_convert(input_path, output_path)

if __name__ == "__main__":
    main()
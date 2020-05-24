# -*- coding:utf-8 -*-
__author__ = "aleimu"
__date__ = "2018-12-6"
__doc__ = "入参校验装饰器"

from flask import Flask, jsonify
from validator import *

app = Flask(__name__)

rules_example = {
    "a": [Required, Equals("123")],  # foo must be exactly equal to 123
    "b": [Required, Truthy()],  # bar must be equivalent to True
    "c": [In(["spam", "eggs", "bacon"])],  # baz must be one of these options
    "d": [Not(Range(1, 100))],  # qux must not be a number between 1 and 100 inclusive
    "e": [Length(0, maximum=5)],
    "f": [Required, InstanceOf(str)],
    "g": [Required, Not(In(["spam", "eggs", "bacon"]))],
    "h": [Required, Pattern("\d\d\%")],
    "i": [Required, GreaterThan(1, reverse=True, auto=True)],  # auto 自动转换成float类型来做比较
    "j": [lambda x: x == "bar"],
    "k": [Required, Isalnum()],  # 判断字符串中只能由字母和数字的组合，不能有特殊符号
    "l": [Required, Isalpha()],  # 字符串里面都是字母，并且至少是一个字母，结果就为真，（汉字也可以）其他情况为假
    "m": [Required, Isdigit()],  # 判断字符串是否全为数字
}



@app.route("/wrap", methods=["GET", "POST", "PUT"])
@validator(rules=rules_example, strip=True)  # 姿势 1:只能检测是否符合规则,不能修改参数,不符合就会直接返回json给调用者
def wrap_example(data):

    return jsonify({"code": 200, "data": data, "err": ""})


@app.route("/func", methods=["GET", "POST", "PUT"])
def func_example():
    result, request_args = validator_func(rules=rules_example, strip=True)  # 姿势 2
    if not result:
        return jsonify({"code": 500, "data": None, "err": request_args})
    a = request_args.get("a")
    b = request_args.get("b")
    c = request_args.get("c")
    d = request_args.get("d")
    e = request_args.get("e")
    f = request_args.get("f")
    g = request_args.get("g")
    h = request_args.get("h")
    i = request_args.get("i")
    j = request_args.get("j")
    k = request_args.get("k")
    l = request_args.get("l")
    m = request_args.get("m")

    return jsonify({"code": 200, "data": None, "err": None})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=6000, debug=True)

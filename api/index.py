from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


marks_data = [
    {"name": "4jOgd1dnJ", "marks": 34},
    {"name": "FY2VwQBDk7", "marks": 8},
    {"name": "dBGO6xdg", "marks": 98},
    {"name": "0c", "marks": 45},
    {"name": "s8L", "marks": 96},
    {"name": "FgJ2Wl", "marks": 0},
    {"name": "7LA", "marks": 1},
    {"name": "s861lUsiK", "marks": 15},
    {"name": "DoF", "marks": 8},
    {"name": "BW", "marks": 30},
    {"name": "W2qFEV5ya", "marks": 78},
    {"name": "D", "marks": 56},
    {"name": "UaEKE", "marks": 24},
    {"name": "A0tdq", "marks": 85},
    {"name": "KG", "marks": 74},
    {"name": "SsILwD6DU", "marks": 18},
    {"name": "aFSApbR8R", "marks": 51},
    {"name": "ojay", "marks": 38},
    {"name": "j5", "marks": 54},
    {"name": "rk", "marks": 85},
    {"name": "Srl84j", "marks": 29},
    {"name": "h", "marks": 40},
    {"name": "C", "marks": 82},
    {"name": "5us5aBpv", "marks": 91},
    {"name": "be2Nc", "marks": 2},
    {"name": "SLXe9cCQiJ", "marks": 17},
    {"name": "l00ys", "marks": 54},
    {"name": "ft", "marks": 2},
    {"name": "oHb", "marks": 98},
    {"name": "nXCEi5", "marks": 64},
    {"name": "NCtg4EhKk", "marks": 4},
    {"name": "W8E", "marks": 24},
    {"name": "V3ZSs", "marks": 16},
    {"name": "U", "marks": 82},
    {"name": "eHUHzj30", "marks": 93},
    {"name": "vRdXAFq", "marks": 82},
    {"name": "phigV", "marks": 73},
    {"name": "C4NrO2Yo", "marks": 91},
    {"name": "kk", "marks": 67},
    {"name": "e2", "marks": 35},
    {"name": "Dxw99fRxbS", "marks": 10},
    {"name": "d19E", "marks": 64},
    {"name": "Lp1KvD", "marks": 53},
    {"name": "AvJ6sTx2", "marks": 24},
    {"name": "WMmai8u1fZ", "marks": 11},
    {"name": "I", "marks": 33},
    {"name": "Le", "marks": 58},
    {"name": "kautFMX", "marks": 46},
    {"name": "U5xWBXzSn", "marks": 10},
    {"name": "gmIHkaWZ", "marks": 37},
    {"name": "ui5j0", "marks": 80},
    {"name": "0oA5iiSK", "marks": 29},
    {"name": "tCOb", "marks": 7},
    {"name": "OO", "marks": 84},
    {"name": "8Y2", "marks": 61},
    {"name": "mio5", "marks": 28},
    {"name": "1J49QJaH", "marks": 33},
    {"name": "Dz8lAv2u", "marks": 58},
    {"name": "yyUcoypK", "marks": 12},
    {"name": "mjeEsN", "marks": 60},
    {"name": "0", "marks": 95},
    {"name": "8pA", "marks": 48},
    {"name": "vBnE3MA4eD", "marks": 72},
    {"name": "aGo", "marks": 28},
    {"name": "H7K", "marks": 99},
    {"name": "hkCTBj", "marks": 66},
    {"name": "FmELB2zo", "marks": 22},
    {"name": "2wOVPfu", "marks": 11},
    {"name": "k8cjUHLMuZ", "marks": 86},
    {"name": "XvKrPYSe", "marks": 18},
    {"name": "KWKT", "marks": 59},
    {"name": "KKP", "marks": 51},
    {"name": "EBYPiDwy08", "marks": 82},
    {"name": "XN6AXv6kzD", "marks": 87},
    {"name": "UvNVwWi", "marks": 95},
    {"name": "IyRUenO", "marks": 25},
    {"name": "9FaiDFZUFs", "marks": 35},
    {"name": "ODt0jtFCq", "marks": 16},
    {"name": "fR9e", "marks": 25},
    {"name": "LFHc9mTkf", "marks": 35},
    {"name": "536", "marks": 86},
    {"name": "zG26i", "marks": 0},
    {"name": "QPAI4R9", "marks": 28},
    {"name": "X8fUB", "marks": 7},
    {"name": "h7D", "marks": 76},
    {"name": "uhUlHN6R8", "marks": 17},
    {"name": "xtxIQl", "marks": 10},
    {"name": "pJGEq", "marks": 42},
    {"name": "Ld1rZNRqM", "marks": 17},
    {"name": "dSYYJi", "marks": 69},
    {"name": "u", "marks": 21},
    {"name": "WuR8cKflf", "marks": 7},
    {"name": "zH", "marks": 99},
    {"name": "IS3jo4", "marks": 18},
    {"name": "RlToSl8Lat", "marks": 37},
    {"name": "Jjz", "marks": 74},
    {"name": "BqxZgJmGCz", "marks": 46},
    {"name": "RFUCfS2m", "marks": 97},
    {"name": "OAUVll4Jl", "marks": 57},
    {"name": "LG", "marks": 97},
]


@app.route("/api", methods=["GET"])
def get_marks():
    names = request.args.getlist("name")
    marks = [
        next(
            (student["marks"] for student in marks_data if student["name"] == name),
            None,
        )
        for name in names
    ]

    return jsonify({"marks": marks})


if __name__ == "__main__":
    app.run(debug=True)

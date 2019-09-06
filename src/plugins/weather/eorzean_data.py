""" 艾欧泽亚天气计算所需数据
"""
import jieba

weatherRateIndex = {
    "0": {
        "id": 0,
        "rates": [{
            "weather": 2,
            "rate": 100
        }]
    },
    "1": {
        "id":
        1,
        "rates": [
            {
                "weather": 7,
                "rate": 5
            }, {
                "weather": 7,
                "rate": 20
            }, {
                "weather": 4,
                "rate": 30
            }, {
                "weather": 3,
                "rate": 40
            }, {
                "weather": 2,
                "rate": 55
            }, {
                "weather": 1,
                "rate": 85
            }, {
                "weather": 2,
                "rate": 100
            }
        ]
    },
    "2": {
        "id":
        2,
        "rates": [
            {
                "weather": 7,
                "rate": 5
            }, {
                "weather": 7,
                "rate": 20
            }, {
                "weather": 4,
                "rate": 30
            }, {
                "weather": 3,
                "rate": 40
            }, {
                "weather": 2,
                "rate": 55
            }, {
                "weather": 1,
                "rate": 85
            }, {
                "weather": 2,
                "rate": 100
            }
        ]
    },
    "3": {
        "id":
        3,
        "rates": [
            {
                "weather": 9,
                "rate": 5
            }, {
                "weather": 7,
                "rate": 20
            }, {
                "weather": 4,
                "rate": 30
            }, {
                "weather": 3,
                "rate": 40
            }, {
                "weather": 2,
                "rate": 55
            }, {
                "weather": 1,
                "rate": 85
            }, {
                "weather": 2,
                "rate": 100
            }
        ]
    },
    "4": {
        "id":
        4,
        "rates": [
            {
                "weather": 9,
                "rate": 5
            }, {
                "weather": 7,
                "rate": 20
            }, {
                "weather": 4,
                "rate": 30
            }, {
                "weather": 3,
                "rate": 40
            }, {
                "weather": 2,
                "rate": 55
            }, {
                "weather": 1,
                "rate": 85
            }, {
                "weather": 2,
                "rate": 100
            }
        ]
    },
    "5": {
        "id":
        5,
        "rates": [
            {
                "weather": 4,
                "rate": 5
            }, {
                "weather": 10,
                "rate": 10
            }, {
                "weather": 9,
                "rate": 25
            }, {
                "weather": 4,
                "rate": 30
            }, {
                "weather": 3,
                "rate": 40
            }, {
                "weather": 2,
                "rate": 70
            }, {
                "weather": 1,
                "rate": 100
            }
        ]
    },
    "6": {
        "id":
        6,
        "rates": [
            {
                "weather": 4,
                "rate": 5
            }, {
                "weather": 8,
                "rate": 10
            }, {
                "weather": 7,
                "rate": 25
            }, {
                "weather": 4,
                "rate": 30
            }, {
                "weather": 3,
                "rate": 40
            }, {
                "weather": 2,
                "rate": 70
            }, {
                "weather": 1,
                "rate": 100
            }
        ]
    },
    "7": {
        "id":
        7,
        "rates": [
            {
                "weather": 1,
                "rate": 40
            }, {
                "weather": 2,
                "rate": 60
            }, {
                "weather": 3,
                "rate": 85
            }, {
                "weather": 4,
                "rate": 95
            }, {
                "weather": 7,
                "rate": 100
            }
        ]
    },
    "8": {
        "id":
        8,
        "rates": [
            {
                "weather": 1,
                "rate": 40
            }, {
                "weather": 2,
                "rate": 60
            }, {
                "weather": 3,
                "rate": 85
            }, {
                "weather": 4,
                "rate": 95
            }, {
                "weather": 7,
                "rate": 100
            }
        ]
    },
    "9": {
        "id":
        9,
        "rates": [
            {
                "weather": 1,
                "rate": 40
            }, {
                "weather": 2,
                "rate": 60
            }, {
                "weather": 3,
                "rate": 85
            }, {
                "weather": 4,
                "rate": 95
            }, {
                "weather": 7,
                "rate": 100
            }
        ]
    },
    "10": {
        "id":
        10,
        "rates": [
            {
                "weather": 11,
                "rate": 15
            }, {
                "weather": 1,
                "rate": 55
            }, {
                "weather": 2,
                "rate": 75
            }, {
                "weather": 3,
                "rate": 85
            }, {
                "weather": 4,
                "rate": 95
            }, {
                "weather": 7,
                "rate": 100
            }
        ]
    },
    "11": {
        "id":
        11,
        "rates": [
            {
                "weather": 1,
                "rate": 40
            }, {
                "weather": 2,
                "rate": 60
            }, {
                "weather": 3,
                "rate": 70
            }, {
                "weather": 4,
                "rate": 80
            }, {
                "weather": 7,
                "rate": 85
            }, {
                "weather": 8,
                "rate": 100
            }
        ]
    },
    "12": {
        "id":
        12,
        "rates": [
            {
                "weather": 14,
                "rate": 20
            }, {
                "weather": 1,
                "rate": 60
            }, {
                "weather": 2,
                "rate": 80
            }, {
                "weather": 3,
                "rate": 90
            }, {
                "weather": 4,
                "rate": 100
            }
        ]
    },
    "13": {
        "id":
        13,
        "rates": [
            {
                "weather": 1,
                "rate": 5
            }, {
                "weather": 2,
                "rate": 20
            }, {
                "weather": 3,
                "rate": 50
            }, {
                "weather": 4,
                "rate": 100
            }
        ]
    },
    "14": {
        "id":
        14,
        "rates": [
            {
                "weather": 3,
                "rate": 20
            }, {
                "weather": 1,
                "rate": 50
            }, {
                "weather": 2,
                "rate": 80
            }, {
                "weather": 4,
                "rate": 90
            }, {
                "weather": 7,
                "rate": 100
            }
        ]
    },
    "15": {
        "id":
        15,
        "rates": [
            {
                "weather": 3,
                "rate": 20
            }, {
                "weather": 1,
                "rate": 50
            }, {
                "weather": 2,
                "rate": 80
            }, {
                "weather": 4,
                "rate": 90
            }, {
                "weather": 7,
                "rate": 100
            }
        ]
    },
    "16": {
        "id":
        16,
        "rates": [
            {
                "weather": 3,
                "rate": 20
            }, {
                "weather": 1,
                "rate": 50
            }, {
                "weather": 2,
                "rate": 70
            }, {
                "weather": 5,
                "rate": 80
            }, {
                "weather": 4,
                "rate": 90
            }, {
                "weather": 7,
                "rate": 100
            }
        ]
    },
    "17": {
        "id":
        17,
        "rates": [
            {
                "weather": 3,
                "rate": 20
            }, {
                "weather": 1,
                "rate": 50
            }, {
                "weather": 2,
                "rate": 70
            }, {
                "weather": 5,
                "rate": 80
            }, {
                "weather": 4,
                "rate": 90
            }, {
                "weather": 7,
                "rate": 100
            }
        ]
    },
    "18": {
        "id":
        18,
        "rates": [
            {
                "weather": 4,
                "rate": 5
            }, {
                "weather": 1,
                "rate": 50
            }, {
                "weather": 2,
                "rate": 80
            }, {
                "weather": 3,
                "rate": 90
            }, {
                "weather": 7,
                "rate": 95
            }, {
                "weather": 8,
                "rate": 100
            }
        ]
    },
    "19": {
        "id":
        19,
        "rates": [
            {
                "weather": 4,
                "rate": 10
            }, {
                "weather": 1,
                "rate": 40
            }, {
                "weather": 2,
                "rate": 60
            }, {
                "weather": 3,
                "rate": 80
            }, {
                "weather": 5,
                "rate": 90
            }, {
                "weather": 6,
                "rate": 100
            }
        ]
    },
    "20": {
        "id":
        20,
        "rates": [
            {
                "weather": 1,
                "rate": 30
            }, {
                "weather": 2,
                "rate": 50
            }, {
                "weather": 3,
                "rate": 70
            }, {
                "weather": 4,
                "rate": 80
            }, {
                "weather": 9,
                "rate": 90
            }, {
                "weather": 10,
                "rate": 100
            }
        ]
    },
    "21": {
        "id":
        21,
        "rates": [
            {
                "weather": 16,
                "rate": 20
            }, {
                "weather": 15,
                "rate": 60
            }, {
                "weather": 2,
                "rate": 70
            }, {
                "weather": 1,
                "rate": 75
            }, {
                "weather": 3,
                "rate": 90
            }, {
                "weather": 4,
                "rate": 100
            }
        ]
    },
    "22": {
        "id":
        22,
        "rates": [
            {
                "weather": 3,
                "rate": 15
            }, {
                "weather": 4,
                "rate": 30
            }, {
                "weather": 17,
                "rate": 60
            }, {
                "weather": 1,
                "rate": 75
            }, {
                "weather": 2,
                "rate": 100
            }
        ]
    },
    "23": {
        "id": 23,
        "rates": [{
            "weather": 29,
            "rate": 100
        }]
    },
    "24": {
        "id":
        24,
        "rates": [
            {
                "weather": 1,
                "rate": 30
            }, {
                "weather": 2,
                "rate": 50
            }, {
                "weather": 3,
                "rate": 70
            }, {
                "weather": 4,
                "rate": 85
            }, {
                "weather": 7,
                "rate": 100
            }
        ]
    },
    "25": {
        "id": 25,
        "rates": [{
            "weather": 26,
            "rate": 100
        }]
    },
    "26": {
        "id": 26,
        "rates": [{
            "weather": 28,
            "rate": 100
        }]
    },
    "27": {
        "id": 27,
        "rates": [{
            "weather": 15,
            "rate": 100
        }]
    },
    "28": {
        "id": 28,
        "rates": [{
            "weather": 3,
            "rate": 100
        }]
    },
    "29": {
        "id":
        29,
        "rates": [
            {
                "weather": 3,
                "rate": 20
            }, {
                "weather": 1,
                "rate": 50
            }, {
                "weather": 2,
                "rate": 80
            }, {
                "weather": 4,
                "rate": 90
            }, {
                "weather": 10,
                "rate": 100
            }
        ]
    },
    "30": {
        "id": 30,
        "rates": [{
            "weather": 27,
            "rate": 100
        }]
    },
    "31": {
        "id": 31,
        "rates": [{
            "weather": 25,
            "rate": 100
        }]
    },
    "32": {
        "id":
        32,
        "rates": [
            {
                "weather": 3,
                "rate": 20
            }, {
                "weather": 1,
                "rate": 50
            }, {
                "weather": 2,
                "rate": 70
            }, {
                "weather": 2,
                "rate": 80
            }, {
                "weather": 4,
                "rate": 90
            }, {
                "weather": 7,
                "rate": 100
            }
        ]
    },
    "33": {
        "id":
        33,
        "rates": [
            {
                "weather": 1,
                "rate": 40
            }, {
                "weather": 2,
                "rate": 60
            }, {
                "weather": 3,
                "rate": 85
            }, {
                "weather": 4,
                "rate": 95
            }, {
                "weather": 7,
                "rate": 100
            }
        ]
    },
    "34": {
        "id":
        34,
        "rates": [
            {
                "weather": 3,
                "rate": 5
            }, {
                "weather": 7,
                "rate": 20
            }, {
                "weather": 4,
                "rate": 30
            }, {
                "weather": 3,
                "rate": 40
            }, {
                "weather": 2,
                "rate": 55
            }, {
                "weather": 1,
                "rate": 85
            }, {
                "weather": 2,
                "rate": 100
            }
        ]
    },
    "35": {
        "id": 35,
        "rates": [{
            "weather": 15,
            "rate": 100
        }]
    },
    "36": {
        "id": 36,
        "rates": [{
            "weather": 5,
            "rate": 100
        }]
    },
    "37": {
        "id": 37,
        "rates": [{
            "weather": 9,
            "rate": 100
        }]
    },
    "38": {
        "id": 38,
        "rates": [{
            "weather": 23,
            "rate": 100
        }]
    },
    "39": {
        "id": 39,
        "rates": [{
            "weather": 24,
            "rate": 100
        }]
    },
    "40": {
        "id": 40,
        "rates": [{
            "weather": 4,
            "rate": 100
        }]
    },
    "41": {
        "id": 41,
        "rates": [{
            "weather": 11,
            "rate": 100
        }]
    },
    "42": {
        "id": 42,
        "rates": [{
            "weather": 16,
            "rate": 100
        }]
    },
    "43": {
        "id": 43,
        "rates": [{
            "weather": 22,
            "rate": 100
        }]
    },
    "44": {
        "id": 44,
        "rates": [{
            "weather": 36,
            "rate": 100
        }]
    },
    "45": {
        "id": 45,
        "rates": [{
            "weather": 20,
            "rate": 100
        }]
    },
    "46": {
        "id": 46,
        "rates": [{
            "weather": 35,
            "rate": 100
        }]
    },
    "47": {
        "id":
        47,
        "rates": [
            {
                "weather": 15,
                "rate": 60
            }, {
                "weather": 2,
                "rate": 70
            }, {
                "weather": 1,
                "rate": 75
            }, {
                "weather": 3,
                "rate": 90
            }, {
                "weather": 4,
                "rate": 100
            }
        ]
    },
    "48": {
        "id":
        48,
        "rates": [
            {
                "weather": 15,
                "rate": 60
            }, {
                "weather": 2,
                "rate": 70
            }, {
                "weather": 1,
                "rate": 75
            }, {
                "weather": 3,
                "rate": 90
            }, {
                "weather": 4,
                "rate": 100
            }
        ]
    },
    "49": {
        "id":
        49,
        "rates": [
            {
                "weather": 16,
                "rate": 20
            }, {
                "weather": 15,
                "rate": 60
            }, {
                "weather": 2,
                "rate": 70
            }, {
                "weather": 1,
                "rate": 75
            }, {
                "weather": 3,
                "rate": 90
            }, {
                "weather": 4,
                "rate": 100
            }
        ]
    },
    "50": {
        "id":
        50,
        "rates": [
            {
                "weather": 3,
                "rate": 10
            }, {
                "weather": 4,
                "rate": 20
            }, {
                "weather": 9,
                "rate": 30
            }, {
                "weather": 11,
                "rate": 40
            }, {
                "weather": 1,
                "rate": 70
            }, {
                "weather": 2,
                "rate": 100
            }
        ]
    },
    "51": {
        "id":
        51,
        "rates": [
            {
                "weather": 3,
                "rate": 10
            }, {
                "weather": 4,
                "rate": 20
            }, {
                "weather": 7,
                "rate": 30
            }, {
                "weather": 8,
                "rate": 40
            }, {
                "weather": 1,
                "rate": 70
            }, {
                "weather": 2,
                "rate": 100
            }
        ]
    },
    "52": {
        "id":
        52,
        "rates": [
            {
                "weather": 3,
                "rate": 10
            }, {
                "weather": 6,
                "rate": 20
            }, {
                "weather": 50,
                "rate": 40
            }, {
                "weather": 1,
                "rate": 70
            }, {
                "weather": 2,
                "rate": 100
            }
        ]
    },
    "53": {
        "id":
        53,
        "rates": [
            {
                "weather": 1,
                "rate": 30
            }, {
                "weather": 2,
                "rate": 60
            }, {
                "weather": 3,
                "rate": 70
            }, {
                "weather": 4,
                "rate": 80
            }, {
                "weather": 5,
                "rate": 90
            }, {
                "weather": 49,
                "rate": 100
            }
        ]
    },
    "54": {
        "id":
        54,
        "rates": [
            {
                "weather": 2,
                "rate": 35
            }, {
                "weather": 3,
                "rate": 70
            }, {
                "weather": 9,
                "rate": 100
            }
        ]
    },
    "55": {
        "id":
        55,
        "rates": [
            {
                "weather": 3,
                "rate": 10
            }, {
                "weather": 4,
                "rate": 20
            }, {
                "weather": 7,
                "rate": 30
            }, {
                "weather": 8,
                "rate": 40
            }, {
                "weather": 1,
                "rate": 70
            }, {
                "weather": 2,
                "rate": 100
            }
        ]
    },
    "56": {
        "id": 56,
        "rates": [{
            "weather": 44,
            "rate": 100
        }]
    },
    "57": {
        "id": 57,
        "rates": [{
            "weather": 51,
            "rate": 100
        }]
    },
    "58": {
        "id": 58,
        "rates": [{
            "weather": 1,
            "rate": 100
        }]
    },
    "59": {
        "id":
        59,
        "rates": [
            {
                "weather": 4,
                "rate": 15
            }, {
                "weather": 7,
                "rate": 40
            }, {
                "weather": 2,
                "rate": 100
            }
        ]
    },
    "60": {
        "id":
        60,
        "rates": [
            {
                "weather": 2,
                "rate": 40
            }, {
                "weather": 4,
                "rate": 75
            }, {
                "weather": 5,
                "rate": 95
            }, {
                "weather": 49,
                "rate": 99
            }, {
                "weather": 54,
                "rate": 100
            }
        ]
    },
    "61": {
        "id":
        61,
        "rates": [
            {
                "weather": 2,
                "rate": 40
            }, {
                "weather": 4,
                "rate": 60
            }, {
                "weather": 5,
                "rate": 95
            }, {
                "weather": 49,
                "rate": 99
            }, {
                "weather": 54,
                "rate": 100
            }
        ]
    },
    "62": {
        "id":
        62,
        "rates": [
            {
                "weather": 2,
                "rate": 40
            }, {
                "weather": 4,
                "rate": 65
            }, {
                "weather": 5,
                "rate": 90
            }, {
                "weather": 49,
                "rate": 98
            }, {
                "weather": 54,
                "rate": 100
            }
        ]
    },
    "63": {
        "id": 63,
        "rates": [{
            "weather": 7,
            "rate": 100
        }]
    },
    "64": {
        "id": 64,
        "rates": [{
            "weather": 2,
            "rate": 60
        }, {
            "weather": 7,
            "rate": 100
        }]
    },
    "65": {
        "id": 65,
        "rates": [{
            "weather": 2,
            "rate": 50
        }, {
            "weather": 7,
            "rate": 100
        }]
    },
    "66": {
        "id": 66,
        "rates": [{
            "weather": 60,
            "rate": 100
        }]
    },
    "67": {
        "id":
        67,
        "rates": [
            {
                "weather": 2,
                "rate": 35
            }, {
                "weather": 15,
                "rate": 65
            }, {
                "weather": 16,
                "rate": 85
            }, {
                "weather": 4,
                "rate": 100
            }
        ]
    },
    "68": {
        "id": 68,
        "rates": [{
            "weather": 14,
            "rate": 100
        }]
    },
    "69": {
        "id": 69,
        "rates": [{
            "weather": 69,
            "rate": 100
        }]
    },
    "70": {
        "id": 70,
        "rates": [{
            "weather": 54,
            "rate": 100
        }]
    },
    "71": {
        "id":
        71,
        "rates": [
            {
                "weather": 2,
                "rate": 30
            }, {
                "weather": 4,
                "rate": 60
            }, {
                "weather": 5,
                "rate": 90
            }, {
                "weather": 49,
                "rate": 100
            }
        ]
    },
    "72": {
        "id": 72,
        "rates": [{
            "weather": 2,
            "rate": 65
        }, {
            "weather": 7,
            "rate": 100
        }]
    },
    "73": {
        "id": 73,
        "rates": [{
            "weather": 2,
            "rate": 65
        }, {
            "weather": 7,
            "rate": 100
        }]
    },
    "74": {
        "id": 74,
        "rates": [{
            "weather": 17,
            "rate": 100
        }]
    },
    "75": {
        "id": 75,
        "rates": [{
            "weather": 74,
            "rate": 100
        }]
    },
    "76": {
        "id": 76,
        "rates": [{
            "weather": 84,
            "rate": 100
        }]
    },
    "77": {
        "id": 77,
        "rates": [{
            "weather": 80,
            "rate": 100
        }]
    },
    "78": {
        "id":
        78,
        "rates": [
            {
                "weather": 1,
                "rate": 15
            }, {
                "weather": 2,
                "rate": 60
            }, {
                "weather": 3,
                "rate": 80
            }, {
                "weather": 4,
                "rate": 90
            }, {
                "weather": 9,
                "rate": 100
            }
        ]
    },
    "79": {
        "id":
        79,
        "rates": [
            {
                "weather": 1,
                "rate": 15
            }, {
                "weather": 2,
                "rate": 60
            }, {
                "weather": 3,
                "rate": 80
            }, {
                "weather": 4,
                "rate": 90
            }, {
                "weather": 9,
                "rate": 100
            }
        ]
    },
    "80": {
        "id":
        80,
        "rates": [
            {
                "weather": 1,
                "rate": 10
            }, {
                "weather": 2,
                "rate": 60
            }, {
                "weather": 3,
                "rate": 75
            }, {
                "weather": 4,
                "rate": 85
            }, {
                "weather": 5,
                "rate": 95
            }, {
                "weather": 11,
                "rate": 100
            }
        ]
    },
    "81": {
        "id":
        81,
        "rates": [
            {
                "weather": 1,
                "rate": 20
            }, {
                "weather": 2,
                "rate": 60
            }, {
                "weather": 3,
                "rate": 80
            }, {
                "weather": 4,
                "rate": 90
            }, {
                "weather": 10,
                "rate": 100
            }
        ]
    },
    "82": {
        "id":
        82,
        "rates": [
            {
                "weather": 7,
                "rate": 10
            }, {
                "weather": 4,
                "rate": 20
            }, {
                "weather": 3,
                "rate": 40
            }, {
                "weather": 2,
                "rate": 80
            }, {
                "weather": 1,
                "rate": 100
            }
        ]
    },
    "83": {
        "id":
        83,
        "rates": [
            {
                "weather": 9,
                "rate": 10
            }, {
                "weather": 5,
                "rate": 20
            }, {
                "weather": 3,
                "rate": 35
            }, {
                "weather": 2,
                "rate": 75
            }, {
                "weather": 1,
                "rate": 100
            }
        ]
    },
    "84": {
        "id":
        84,
        "rates": [
            {
                "weather": 8,
                "rate": 5
            }, {
                "weather": 7,
                "rate": 15
            }, {
                "weather": 4,
                "rate": 25
            }, {
                "weather": 3,
                "rate": 40
            }, {
                "weather": 2,
                "rate": 80
            }, {
                "weather": 1,
                "rate": 100
            }
        ]
    },
    "85": {
        "id":
        85,
        "rates": [
            {
                "weather": 6,
                "rate": 5
            }, {
                "weather": 5,
                "rate": 10
            }, {
                "weather": 7,
                "rate": 17
            }, {
                "weather": 4,
                "rate": 25
            }, {
                "weather": 3,
                "rate": 35
            }, {
                "weather": 2,
                "rate": 75
            }, {
                "weather": 1,
                "rate": 100
            }
        ]
    },
    "86": {
        "id": 86,
        "rates": [{
            "weather": 50,
            "rate": 100
        }]
    },
    "87": {
        "id": 87,
        "rates": [{
            "weather": 82,
            "rate": 100
        }]
    },
    "88": {
        "id": 88,
        "rates": [{
            "weather": 79,
            "rate": 100
        }]
    },
    "89": {
        "id": 89,
        "rates": [{
            "weather": 88,
            "rate": 100
        }]
    },
    "90": {
        "id": 90,
        "rates": [{
            "weather": 2,
            "rate": 100
        }]
    },
    "91": {
        "id":
        91,
        "rates": [
            {
                "weather": 2,
                "rate": 30
            }, {
                "weather": 6,
                "rate": 60
            }, {
                "weather": 8,
                "rate": 90
            }, {
                "weather": 15,
                "rate": 100
            }
        ]
    },
    "92": {
        "id": 92,
        "rates": [{
            "weather": 77,
            "rate": 100
        }]
    },
    "93": {
        "id": 93,
        "rates": [{
            "weather": 92,
            "rate": 100
        }]
    },
    "94": {
        "id":
        94,
        "rates": [
            {
                "weather": 2,
                "rate": 10
            }, {
                "weather": 4,
                "rate": 28
            }, {
                "weather": 14,
                "rate": 46
            }, {
                "weather": 15,
                "rate": 64
            }, {
                "weather": 9,
                "rate": 82
            }, {
                "weather": 16,
                "rate": 100
            }
        ]
    },
    "95": {
        "id": 95,
        "rates": [{
            "weather": 101,
            "rate": 100
        }]
    },
    "96": {
        "id":
        96,
        "rates": [
            {
                "weather": 2,
                "rate": 10
            }, {
                "weather": 14,
                "rate": 28
            }, {
                "weather": 9,
                "rate": 46
            }, {
                "weather": 16,
                "rate": 64
            }, {
                "weather": 49,
                "rate": 82
            }, {
                "weather": 15,
                "rate": 100
            }
        ]
    },
    "97": {
        "id": 97,
        "rates": [{
            "weather": 12,
            "rate": 100
        }]
    },
    "98": {
        "id": 98,
        "rates": [{
            "weather": 102,
            "rate": 100
        }]
    },
    "99": {
        "id": 99,
        "rates": [{
            "weather": 113,
            "rate": 100
        }]
    },
    "100": {
        "id":
        100,
        "rates": [
            {
                "weather": 2,
                "rate": 12
            }, {
                "weather": 8,
                "rate": 34
            }, {
                "weather": 17,
                "rate": 56
            }, {
                "weather": 10,
                "rate": 78
            }, {
                "weather": 15,
                "rate": 100
            }
        ]
    },
    "101": {
        "id": 101,
        "rates": [{
            "weather": 119,
            "rate": 100
        }]
    }
}

locationIndex = {
    "21": {
        "id": 21,
        "name": "艾欧泽亚",
        "mapSize": 1
    },
    "22": {
        "id": 22,
        "name": "拉诺西亚",
        "mapSize": 1,
        "zones": [27, 30, 31, 32, 33, 34, 350, 358, 425]
    },
    "23": {
        "id": 23,
        "name": "黑衣森林",
        "mapSize": 1,
        "zones": [51, 54, 55, 56, 57, 426]
    },
    "24": {
        "id": 24,
        "name": "萨纳兰",
        "mapSize": 1,
        "zones": [39, 42, 43, 44, 45, 46, 427]
    },
    "25": {
        "id": 25,
        "name": "库尔札斯",
        "mapSize": 1,
        "zones": [62, 63, 2200]
    },
    "26": {
        "id": 26,
        "name": "摩杜纳",
        "parentId": 26,
        "mapSize": 1,
        "zones": [67]
    },
    "27": {
        "id": 27,
        "name": "利姆萨·罗敏萨",
        "parentId": 22,
        "weatherRate": 14
    },
    "8888": {
        "id":
        8888,
        "name":
        "讨伐歼灭战",
        "mapSize":
        1,
        "zones": [
            357, 361, 359, 360, 477, 1334, 1363, 1399, 133, 406, 2151, 2081,
            2178, 2256, 2265, 2266, 2295, 2299
        ]
    },
    "8889": {
        "id": 8889,
        "name": "纷争前线",
        "mapSize": 1,
        "zones": [496, 1740]
    },
    "8891": {
        "id": 8891,
        "name": "大型任务&其他",
        "mapSize": 1,
        "zones": [1409, 1868, 1960, 2181, 2284]
    },
    "8892": {
        "id": 8892,
        "name": "优雷卡",
        "mapSize": 1,
        "zones": [2414, 2462, 2530, 2545]
    },
    "30": {
        "id": 30,
        "name": "中拉诺西亚",
        "parentId": 22,
        "mapSize": 1,
        "weatherRate": 16
    },
    "31": {
        "id": 31,
        "name": "拉诺西亚低地",
        "parentId": 22,
        "mapSize": 1,
        "weatherRate": 17
    },
    "32": {
        "id": 32,
        "name": "东拉诺西亚",
        "parentId": 22,
        "mapSize": 1,
        "weatherRate": 18
    },
    "33": {
        "id": 33,
        "name": "西拉诺西亚",
        "parentId": 22,
        "mapSize": 1,
        "weatherRate": 19
    },
    "34": {
        "id": 34,
        "name": "拉诺西亚高地",
        "parentId": 22,
        "mapSize": 1,
        "weatherRate": 20
    },
    "39": {
        "id": 39,
        "name": "乌尔达哈",
        "parentId": 24,
        "weatherRate": 7
    },
    "42": {
        "id": 42,
        "name": "西萨纳兰",
        "parentId": 24,
        "mapSize": 1,
        "weatherRate": 9
    },
    "43": {
        "id": 43,
        "name": "中萨纳兰",
        "parentId": 24,
        "mapSize": 1,
        "weatherRate": 10
    },
    "44": {
        "id": 44,
        "name": "东萨纳兰",
        "parentId": 24,
        "mapSize": 1,
        "weatherRate": 11
    },
    "45": {
        "id": 45,
        "name": "南萨纳兰",
        "parentId": 24,
        "mapSize": 1,
        "weatherRate": 12
    },
    "46": {
        "id": 46,
        "name": "北萨纳兰",
        "parentId": 24,
        "mapSize": 1,
        "weatherRate": 13
    },
    "51": {
        "id": 51,
        "name": "格里达尼亚",
        "parentId": 23,
        "weatherRate": 1
    },
    "54": {
        "id": 54,
        "name": "黑衣森林中央林区",
        "parentId": 23,
        "mapSize": 1,
        "weatherRate": 3
    },
    "55": {
        "id": 55,
        "name": "黑衣森林东部林区",
        "parentId": 23,
        "mapSize": 1,
        "weatherRate": 4
    },
    "56": {
        "id": 56,
        "name": "黑衣森林南部林区",
        "parentId": 23,
        "mapSize": 1,
        "weatherRate": 5
    },
    "57": {
        "id": 57,
        "name": "黑衣森林北部林区",
        "parentId": 23,
        "mapSize": 1,
        "weatherRate": 6
    },
    "62": {
        "id": 62,
        "name": "伊修加德",
        "parentId": 25,
        "mapSize": 1,
        "weatherRate": 48
    },
    "63": {
        "id": 63,
        "name": "库尔札斯中央高地",
        "parentId": 25,
        "mapSize": 1,
        "weatherRate": 21
    },
    "67": {
        "id": 67,
        "name": "摩杜纳",
        "parentId": 26,
        "mapSize": 1,
        "weatherRate": 22
    },
    "128": {
        "id": 128,
        "name": "邪教驻地无限城古堡",
        "parentId": 8888,
        "mapSize": 2.0,
        "weatherRate": 28
    },
    "133": {
        "id": 133,
        "name": "兀尔德恩惠地·奥丁",
        "parentId": 8888,
        "size": 1.0,
        "weatherRate": 45
    },
    "230": {
        "id": 230,
        "name": "领航明灯天狼星灯塔",
        "parentId": 8888,
        "mapSize": 2.0,
        "weatherRate": 28
    },
    "350": {
        "id": 350,
        "name": "拉诺西亚外地",
        "parentId": 22,
        "mapSize": 1,
        "weatherRate": 24
    },
    "357": {
        "id": 357,
        "name": "炎帝陵",
        "parentId": 8888,
        "mapSize": 4.0,
        "weatherRate": 25
    },
    "358": {
        "id": 358,
        "name": "狼狱停船场",
        "parentId": 22,
        "mapSize": 4.0,
        "weatherRate": 29
    },
    "359": {
        "id": 359,
        "name": "奥·哥摩罗火口神殿",
        "parentId": 8888,
        "mapSize": 4.0,
        "weatherRate": 23
    },
    "360": {
        "id": 360,
        "name": "荆棘之园",
        "parentId": 8888,
        "mapSize": 4.0,
        "weatherRate": 30
    },
    "361": {
        "id": 361,
        "name": "呼啸眼石塔群",
        "parentId": 8888,
        "mapSize": 4.0,
        "weatherRate": 26
    },
    "401": {
        "id": 401,
        "name": "石卫塔",
        "parentId": 8888,
        "mapSize": 2.0,
        "weatherRate": 27
    },
    "404": {
        "id": 404,
        "name": "披雪大冰壁",
        "parentId": 8888,
        "mapSize": 2.0,
        "weatherRate": 42
    },
    "406": {
        "id": 406,
        "name": "云廊",
        "parentId": 8888,
        "mapSize": 2.0,
        "weatherRate": 28
    },
    "418": {
        "id": 418,
        "name": "密约之塔",
        "parentId": 8888,
        "mapSize": 2.0,
        "weatherRate": 74
    },
    "425": {
        "id": 425,
        "name": "海雾村",
        "parentId": 22,
        "mapSize": 2,
        "weatherRate": 32
    },
    "426": {
        "id": 426,
        "name": "薰衣草苗圃",
        "parentId": 23,
        "mapSize": 2,
        "weatherRate": 34
    },
    "427": {
        "id": 427,
        "name": "高脚孤丘",
        "parentId": 24,
        "mapSize": 2,
        "weatherRate": 33
    },
    "477": {
        "id": 477,
        "name": "后营门",
        "parentId": 8888,
        "mapSize": 4.0,
        "weatherRate": 31
    },
    "496": {
        "id": 496,
        "name": "尘封秘岩",
        "parentId": 8889,
        "mapSize": 1.0,
        "weatherRate": 59
    },
    "497": {
        "id": 497,
        "name": "阿巴拉提亚",
        "mapSize": 2,
        "zones": [2100, 2101, 1647]
    },
    "498": {
        "id": 498,
        "name": "龙堡",
        "mapSize": 2,
        "zones": [2000, 2001, 2002, 2082]
    },
    "1302": {
        "id": 1302,
        "name": "The Outer Coil - Incubation Bay",
        "parentId": 8888,
        "mapSize": 2.0,
        "weatherRate": 28
    },
    "1334": {
        "id": 1334,
        "name": "对利维亚桑双体船",
        "parentId": 8888,
        "mapSize": 4.0,
        "weatherRate": 38
    },
    "1363": {
        "id": 1363,
        "name": "神判古树",
        "parentId": 8888,
        "size": 4.0,
        "weatherRate": 43
    },
    "1399": {
        "id": 1399,
        "name": "无尽轮回剧场",
        "parentId": 8888,
        "size": 4.0,
        "weatherRate": 46
    },
    "1409": {
        "id": 1409,
        "name": "龙炎核心",
        "parentId": 8891,
        "size": 2.0,
        "weatherRate": 44
    },
    "1647": {
        "id": 1647,
        "name": "云冠群岛",
        "parentId": 497,
        "mapSize": 1,
        "weatherRate": 71
    },
    "1740": {
        "id": 1740,
        "name": "荣誉野",
        "parentId": 8889,
        "size": 1.0,
        "weatherRate": 67
    },
    "1792": {
        "id": 1792,
        "name": "塞尔法特尔溪谷",
        "parentId": 8888,
        "size": 2.0,
        "weatherRate": 40
    },
    "1857": {
        "id": 1857,
        "name": "巴埃萨长城",
        "parentId": 8888,
        "size": 2.0,
        "weatherRate": 40
    },
    "1868": {
        "id": 1868,
        "name": "拉德莉亚女士号",
        "parentId": 8891,
        "size": 2.0,
        "weatherRate": 58
    },
    "1960": {
        "id": 1960,
        "name": "惨境号",
        "parentId": 8891,
        "size": 4.0,
        "weatherRate": 36
    },
    "2000": {
        "id": 2000,
        "name": "龙堡参天高地",
        "parentId": 498,
        "mapSize": 1,
        "weatherRate": 50
    },
    "2001": {
        "id": 2001,
        "name": "龙堡内陆低地",
        "parentId": 498,
        "mapSize": 1,
        "weatherRate": 51
    },
    "2002": {
        "id": 2002,
        "name": "翻云雾海",
        "parentId": 498,
        "mapSize": 1,
        "weatherRate": 52
    },
    "2050": {
        "id": 2050,
        "name": "邪龙王座龙巢神殿",
        "parentId": 8888,
        "size": 2.0,
        "weatherRate": 28
    },
    "2081": {
        "id": 2081,
        "name": "武神斗技场",
        "parentId": 8888,
        "size": 4.0,
        "weatherRate": 57
    },
    "2082": {
        "id": 2082,
        "name": "田园郡",
        "parentId": 498,
        "mapSize": 1,
        "weatherRate": 55
    },
    "2100": {
        "id": 2100,
        "name": "阿巴拉提亚云海",
        "parentId": 497,
        "mapSize": 1,
        "weatherRate": 53
    },
    "2101": {
        "id": 2101,
        "name": "魔大陆阿济兹拉",
        "parentId": 497,
        "mapSize": 1,
        "weatherRate": 54
    },
    "2151": {
        "id": 2151,
        "name": "无尽苍空",
        "parentId": 8888,
        "size": 4.0,
        "weatherRate": 28
    },
    "2178": {
        "id": 2178,
        "name": "奇点反应堆",
        "parentId": 8888,
        "size": 4.0,
        "weatherRate": 56
    },
    "2181": {
        "id": 2181,
        "name": "魔航船虚无方舟-上甲板",
        "parentId": 8891,
        "size": 2.0,
        "weatherRate": 37
    },
    "2200": {
        "id": 2200,
        "name": "库尔札斯西部高地",
        "parentId": 25,
        "mapSize": 1,
        "weatherRate": 49
    },
    "2214": {
        "id": 2214,
        "name": "暮卫塔",
        "parentId": 8888,
        "size": 2.0,
        "weatherRate": 42
    },
    "2256": {
        "id": 2256,
        "name": "抑制绝境S1T7",
        "parentId": 8888,
        "size": 4.0,
        "weatherRate": 66
    },
    "2265": {
        "id": 2265,
        "name": "抑制绝境P1T6",
        "parentId": 8888,
        "size": 4.0,
        "weatherRate": 69
    },
    "2266": {
        "id": 2266,
        "name": "抑制绝境Z1T9",
        "parentId": 8888,
        "size": 4.0,
        "weatherRate": 75
    },
    "2284": {
        "id": 2284,
        "name": "次元城地下牢狱",
        "parentId": 8891,
        "size": 2.0,
        "weatherRate": 88
    },
    "2295": {
        "id": 2295,
        "name": "宝物库",
        "parentId": 8888,
        "size": 4.0,
        "weatherRate": 77
    },
    "2297": {
        "id": 2297,
        "name": "妖歌海",
        "parentId": 22,
        "size": 2.0,
        "weatherRate": 36
    },
    "2299": {
        "id": 2299,
        "name": "美神地下神殿",
        "parentId": 8888,
        "size": 4.0,
        "weatherRate": 87
    },
    "2400": {
        "id": 2400,
        "name": "基拉巴尼亚",
        "mapSize": 2,
        "zones": [2403, 2406, 2407, 2408]
    },
    "2401": {
        "id": 2401,
        "name": "奥萨德",
        "parentId": 2401,
        "mapSize": 1.0,
        "zones": [2409, 2410, 2411]
    },
    "2402": {
        "id": 2402,
        "name": "远东之国",
        "mapSize": 2,
        "zones": [2404, 2412]
    },
    "2403": {
        "id": 2403,
        "name": "神拳痕",
        "parentId": 2400,
        "mapSize": 2,
        "weatherRate": 78
    },
    "2404": {
        "id": 2404,
        "name": "黄金港",
        "parentId": 2402,
        "mapSize": 2,
        "weatherRate": 82
    },
    "2405": {
        "id": 2405,
        "name": "优雷卡"
    },
    "2406": {
        "id": 2406,
        "name": "基拉巴尼亚边区",
        "parentId": 2400,
        "mapSize": 1,
        "weatherRate": 79
    },
    "2407": {
        "id": 2407,
        "name": "基拉巴尼亚山区",
        "parentId": 2400,
        "mapSize": 1,
        "weatherRate": 80
    },
    "2408": {
        "id": 2408,
        "name": "基拉巴尼亚湖区",
        "parentId": 2400,
        "mapSize": 1,
        "weatherRate": 81
    },
    "2409": {
        "id": 2409,
        "name": "红玉海",
        "parentId": 2401,
        "mapSize": 1.0,
        "weatherRate": 83
    },
    "2410": {
        "id": 2410,
        "name": "延夏",
        "parentId": 2401,
        "mapSize": 1.0,
        "weatherRate": 84
    },
    "2411": {
        "id": 2411,
        "name": "太阳神草原",
        "parentId": 2401,
        "mapSize": 1.0,
        "weatherRate": 85
    },
    "2412": {
        "id": 2412,
        "name": "白银乡",
        "parentId": 2402,
        "mapSize": 2,
        "weatherRate": 82
    },
    "2414": {
        "id": 2414,
        "name": "常风之地",
        "parentId": 2405,
        "weatherRate": 91
    },
    "2462": {
        "id": 2462,
        "name": "恒冰之地",
        "parentId": 2405,
        "weatherRate": 94
    },
    "2530": {
        "id": 2530,
        "name": "涌火之地",
        "parentId": 2405,
        "weatherRate": 96
    },
    "2545": {
        "id": 2545,
        "name": "丰水之地",
        "parentId": 2405,
        "weatherRate": 100
    }
}

weatherIndex = [
    "", "碧空", "晴朗", "阴云", "薄雾", "微风", "强风", "小雨", "暴雨", "打雷", "雷雨", "扬沙",
    "Sandstorms", "HotSpells", "热浪", "小雪", "暴雪", "妖雾", "Auroras", "暗黑", "绝命",
    "阴云", "雷云", "RoughSeas", "RoughSeas", "Louring", "热浪", "妖雾", "强风", "烟雾",
    "晴朗", "晴朗", "晴朗", "晴朗", "晴朗", "极光", "辉核", "辉核", "辉核", "辉核", "ShelfClouds",
    "ShelfClouds", "ShelfClouds", "ShelfClouds", "神意", "神意", "神意", "神意", "神意",
    "灵风", "灵电", "烟武", "晴朗", "RoyalLevin", "Hyperelectricity", "RoyalLevin",
    "神意", "打雷", "打雷", "CutScene", "神秘", "神秘", "小雨", "晴朗", "小雨", "晴朗",
    "Dragonstorms", "Dragonstorms", "Subterrain", "平衡", "平衡", "BeyondTime",
    "BeyondTime", "BeyondTime", "鬼气", "鬼气", "鬼气", "次元", "次元", "次元", "豪雨", "豪雨",
    "极乐", "极乐", "Wyrmstorms", "Wyrmstorms", "豪雨", "Quicklevin", "打雷", "次元",
    "晴朗", "碧空", "白旋风", "白旋风", "白旋风", "Ultimania", "白旋风", "Moonlight",
    "Moonlight", "Moonlight", "Moonlight", "晴朗", "Scarlet", "Scarlet",
    "Scarlet", "晴朗", "晴朗", "晴朗", "晴朗", "Flames", "Tsunamis", "Cyclones",
    "Geostorms", "TrueBlue", "TrueBlue", "TrueBlue", "UmbralTurbulence",
    "TrueBlue", "", "", "", ""
]

# 添加艾欧泽亚的地名到结巴分词中
for index in locationIndex:
    jieba.add_word(locationIndex[index]["name"], tag='ns')

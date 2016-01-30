import billboard
import json
import sys


if __name__ == '__main__':
	if sys.argv[2]:
		date = sys.argv[2]
		filename = sys.argv[1] + "-" + sys.argv[2] + ".json"
	else:
		date = null
		filename = sys.argv[1] + ".json"
	# 'hot-100', '2015-11-28'
	chart = billboard.ChartData(sys.argv[1], date=date)
	chart.to_JSON(filename)
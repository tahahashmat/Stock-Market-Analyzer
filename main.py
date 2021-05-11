# IMPORTS
import yfinance as yf
import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

##############
## UI CLASS ##
##############
class Ui_MainWindow(object):
    def setupUi(self, MainWindow, top, bottom):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 440)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 440))
        MainWindow.setMaximumSize(QtCore.QSize(800, 440))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setIconSize(QtCore.QSize(24, 24))
        MainWindow.setAnimated(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(800, 440))
        self.centralwidget.setMaximumSize(QtCore.QSize(800, 440))
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setEnabled(True)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 780, 40))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setMinimumSize(QtCore.QSize(780, 40))
        self.textBrowser.setMaximumSize(QtCore.QSize(780, 40))
        self.textBrowser.setFocusPolicy(QtCore.Qt.NoFocus)
        self.textBrowser.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser.setAcceptRichText(True)
        self.textBrowser.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.textBrowser.setOpenLinks(False)
        self.textBrowser.setObjectName("textBrowser")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setEnabled(True)
        self.listWidget.setGeometry(QtCore.QRect(10, 70, 380, 350))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setMinimumSize(QtCore.QSize(380, 350))
        self.listWidget.setMaximumSize(QtCore.QSize(380, 350))

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.PlaceholderText, brush)

        self.listWidget.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.listWidget.setFont(font)
        self.listWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.listWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.listWidget.setLineWidth(1)
        self.listWidget.setMidLineWidth(0)
        self.listWidget.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget.setAutoScroll(False)
        self.listWidget.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listWidget.setProperty("showDropIndicator", False)
        self.listWidget.setDefaultDropAction(QtCore.Qt.CopyAction)
        self.listWidget.setSelectionMode(
            QtWidgets.QAbstractItemView.NoSelection)
        self.listWidget.setMovement(QtWidgets.QListView.Static)
        self.listWidget.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.listWidget.setViewMode(QtWidgets.QListView.ListMode)
        self.listWidget.setObjectName("listWidget")

        for x in range(len(top)):
            item = QtWidgets.QListWidgetItem()
            item.setText(
                (str(x+1) + ": " + str(top[x][0]) + " | " + str(top[x][1])))
            self.listWidget.addItem(item)

        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setEnabled(True)
        self.listWidget_2.setGeometry(QtCore.QRect(410, 70, 380, 350))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.listWidget_2.sizePolicy().hasHeightForWidth())
        self.listWidget_2.setSizePolicy(sizePolicy)
        self.listWidget_2.setMinimumSize(QtCore.QSize(380, 350))
        self.listWidget_2.setMaximumSize(QtCore.QSize(380, 350))

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.PlaceholderText, brush)
        self.listWidget_2.setPalette(palette)

        self.listWidget_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.listWidget_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.listWidget_2.setLineWidth(1)
        self.listWidget_2.setMidLineWidth(0)
        self.listWidget_2.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget_2.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget_2.setAutoScroll(False)
        self.listWidget_2.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listWidget_2.setProperty("showDropIndicator", False)
        self.listWidget_2.setDefaultDropAction(QtCore.Qt.CopyAction)
        self.listWidget_2.setSelectionMode(
            QtWidgets.QAbstractItemView.NoSelection)
        self.listWidget_2.setMovement(QtWidgets.QListView.Static)
        self.listWidget_2.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.listWidget_2.setViewMode(QtWidgets.QListView.ListMode)
        self.listWidget_2.setObjectName("listWidget_2")

        for x in range(len(bottom)):
            item = QtWidgets.QListWidgetItem()
            item.setText(
                (str(x+1) + ": " + str(bottom[x][0]) + " | " + str(bottom[x][1])))
            self.listWidget_2.addItem(item)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 50, 100, 20))
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setAlignment(QtCore.Qt.AlignLeading |
                                QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(410, 50, 100, 20))
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_2.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_2.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "AI STOCK PREDICTOR"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600;\">AI STOCK PREDICTOR</span></p></body></html>"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.listWidget.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        self.listWidget_2.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("MainWindow", "TOP STOCKS"))
        self.label_2.setText(_translate("MainWindow", "BOTTOM STOCKS"))

#-- END OF UI CLASS ----------------------------------------------------------------------------------------------------#


######################
## GET EMA FUNCTION ##
######################
def getEMA(last_100):
    previousfiftyday = 0
    previousTwentyDay = 0
    previousTenDay = 0
    previousFiveDay = 0

    dayfiftytohundredSMA = 0
    daytwentytofourtySMA = 0
    daytentotwentySMA = 0
    dayfivetotenSMA = 0

    ema_list = []

    x = len(last_100) - 6
    while x >= 90:
        dayfivetotenSMA += last_100[x]
        x -= 1
    dayfivetotenSMA = dayfivetotenSMA/5

    x = len(last_100) - 11
    while x >= 80:
        daytentotwentySMA += last_100[x]
        x -= 1
    daytentotwentySMA = daytentotwentySMA/10

    x = len(last_100) - 21
    while x >= 60:
        daytwentytofourtySMA += last_100[x]
        x -= 1
    daytwentytofourtySMA = daytwentytofourtySMA/20

    x = len(last_100) - 51
    while x >= 0:
        dayfiftytohundredSMA += last_100[x]
        x -= 1
    dayfiftytohundredSMA = dayfiftytohundredSMA/50

    fivedaysmoothingConstant = 2 / (5 + 1)
    tendaysmoothingConstant = 2 / (10 + 1)
    twentydaysmoothingConstant = 2 / (20 + 1)
    fiftydaysmoothingConstant = 2 / (50 + 1)

    fiftydayEMA = (last_100[51] - dayfiftytohundredSMA) * \
        fiftydaysmoothingConstant + dayfiftytohundredSMA
    twentydayEMA = (last_100[81] - daytwentytofourtySMA) * \
        twentydaysmoothingConstant + daytwentytofourtySMA
    tendayEMA = (last_100[91] - daytentotwentySMA) * \
        tendaysmoothingConstant + daytentotwentySMA
    fivedayEMA = (last_100[96] - dayfivetotenSMA) * \
        fivedaysmoothingConstant + dayfivetotenSMA

    x = len(last_100) - 48
    while x < len(last_100):
        fiftydayEMA = (
            last_100[x] - fiftydayEMA) * fiftydaysmoothingConstant + fiftydayEMA
        x += 1

    x = len(last_100) - 18
    while x < len(last_100):
        twentydayEMA = (
            last_100[x] - twentydayEMA) * twentydaysmoothingConstant + twentydayEMA
        x += 1

    x = len(last_100) - 8
    while x < len(last_100):
        tendayEMA = (last_100[x] -
                     tendayEMA) * tendaysmoothingConstant + tendayEMA
        x += 1

    x = len(last_100) - 3
    while x < len(last_100):
        fivedayEMA = (last_100[x] -
                      fivedayEMA) * fivedaysmoothingConstant + fivedayEMA
        x += 1

    ema_list.append(fivedayEMA)
    ema_list.append(tendayEMA)
    ema_list.append(twentydayEMA)
    ema_list.append(fiftydayEMA)

    return ema_list

#-- END OF EMA FUNCTION ----------------------------------------------------------------------------------------------------#

######################
## GET RSI FUNCTION ##
######################
def getRSI(last_15):
    averageUp = 0
    totalUp = 0
    averageDown = 0
    totalDown = 0
    n = 15
    rsi = 0
    x = 1
    y = 0

    while x <= len((last_15)) - 1:
        if last_15[x] > last_15[y]:
            totalUp += (last_15[x] - last_15[y]/last_15[y])
        else:
            totalDown += (last_15[x] - last_15[y]/last_15[y])
        x += 1
        y += 1

    averageUp = totalUp/n
    averageDown = totalDown/n

    rsi = 100 - (100/((1+(averageUp/averageDown))))

    return rsi

#-- END OF RSI FUNCTION ----------------------------------------------------------------------------------------------------#


# 5 diff functions for 5 diff indicators

# function 1 which takes in SMA, EMA. Function determines when a crossover happens between the moving averages (SMA and EMA) For example if 5 day SMA crosses over 10 day SMA
# it is bullish (strong uptrend) or 10 day crosses 15 day (bullish), etc. If it goes down that is 5 day doesnt cross the 10 day moving averages it is downtrend

def crossover(SMAvalues, EMAvalues):
    crossover_trendpoints = 0

    # upside EMA points
    if EMAvalues[0] > EMAvalues[1]:
        crossover_trendpoints += 0.3

    if EMAvalues[1] > EMAvalues[2]:
        crossover_trendpoints += 0.2

    if EMAvalues[2] > EMAvalues[3]:
        crossover_trendpoints += 0.1

    # downside EMA points
    if EMAvalues[0] < EMAvalues[1]:
        crossover_trendpoints -= 0.3

    if EMAvalues[1] < EMAvalues[2]:
        crossover_trendpoints -= 0.2

    if EMAvalues[2] < EMAvalues[3]:
        crossover_trendpoints -= 0.1

    # upside SMA points
    if SMAvalues[0] > SMAvalues[1]:
        crossover_trendpoints += 0.2

    if SMAvalues[1] > SMAvalues[2]:
        crossover_trendpoints += 0.125

    if SMAvalues[2] > SMAvalues[3]:
        crossover_trendpoints += 0.075

    # downside SMA points
    if SMAvalues[0] < SMAvalues[1]:
        crossover_trendpoints -= 0.2

    if SMAvalues[1] < SMAvalues[2]:
        crossover_trendpoints -= 0.125

    if SMAvalues[2] < SMAvalues[3]:
        crossover_trendpoints -= 0.075

    return crossover_trendpoints

# function 2 to find price above average (takes in closing price, SMA, EMA) i.e. if the closing price is above the 10 day SMA, EMA good if below bad


def price_above_average(price, EMAvalues, SMAvalues):
    price_above_average_points = 0

    # upside EMA trend
    if price > EMAvalues[0]:
        price_above_average_points += 0.225

    if price > EMAvalues[1]:
        price_above_average_points += 0.175

    if price > EMAvalues[2]:
        price_above_average_points += 0.125

    if price > EMAvalues[3]:
        price_above_average_points += 0.075

    # downside EMA trends
    if price < EMAvalues[0]:
        price_above_average_points -= 0.225

    if price < EMAvalues[1]:
        price_above_average_points -= 0.175

    if price < EMAvalues[2]:
        price_above_average_points -= 0.125

    if price < EMAvalues[3]:
        price_above_average_points -= 0.075

    # upside SMA trend
    if price > SMAvalues[0]:
        price_above_average_points += 0.175

    if price > SMAvalues[1]:
        price_above_average_points += 0.125

    if price > SMAvalues[2]:
        price_above_average_points += 0.075

    if price > SMAvalues[3]:
        price_above_average_points += 0.025

    # downside SMA trend
    if price < SMAvalues[0]:
        price_above_average_points -= 0.175

    if price < SMAvalues[1]:
        price_above_average_points -= 0.125

    if price < SMAvalues[2]:
        price_above_average_points -= 0.075

    if price < SMAvalues[3]:
        price_above_average_points -= 0.025

    return price_above_average_points


# funtion 3 that takes in rsi value, tells you whether stock is over bought or over sold. A stock over 70 RSI is overbought, stock below 30 is beneficial, between 30 and 70 is meh

def rsi(RSIvalue):

    rsi_trendpoints = 0
    givenrsi = RSIvalue

    if givenrsi < 50:
        rsi_trendpoints = (1 - (givenrsi/100) * 2) * 1

    if givenrsi >= 50:
        rsi_trendpoints = (1 - (givenrsi/100) * 2) * 1

    return rsi_trendpoints


# function 4 that takes in roc, which says the closert the roc is to 0 and positive/negative, the less strong it is, if roc >> 0 then strong, if roc << 0 then bad

def roc(ROCvalues):

    day5_trendpoint = 0
    day10_trendpoint = 0
    day15_trendpoint = 0
    roc_trendpoints = 0
    roc_dayFive = 0
    roc_dayTen = 0
    roc_dayFifteen = 0

    roc_dayFive = ROCvalues[0]
    roc_dayTen = ROCvalues[1]
    roc_dayFifteen = ROCvalues[2]

    day5_trendpoint = roc_dayFive * 0.5
    day10_trendpoint = roc_dayTen * 0.3
    day15_trendpoint = roc_dayFifteen * 0.2

    roc_trendpoints = day5_trendpoint + day10_trendpoint + day15_trendpoint

    return roc_trendpoints


# function 5 that takes in closing price, EMA, SMA, average volumes, current volume. if input from function 1 is uptrend with low volume not good, if above uptrend with strong volume good
# downtrend on weaker volume then good, downtrend on strong volume then bad

def average_volume(price, SMAvalues, EMAvalues, currentvolume, averagevolume):

    trend = (price_above_average(price, SMAvalues, EMAvalues) +
             crossover(SMAvalues, EMAvalues))/2
    total = 0
    total_points = 0

    if currentvolume > averagevolume[2]:
        total += 0.5
    if currentvolume > averagevolume[1]:
        total += 0.3
    if currentvolume > averagevolume[0]:
        total += 0.2

    if currentvolume < averagevolume[2]:
        total -= 0.5
    if currentvolume < averagevolume[1]:
        total -= 0.3
    if currentvolume < averagevolume[0]:
        total -= 0.2

    total_points = trend * total

    return total_points


def get_total_trend_points(ticker):
    totalTrendpoints = 0

    closeByDay = ticker['Close']
    volumeByDay = ticker['Volume']

    lastClosingPrice = closeByDay[-1]
    lastVolume = volumeByDay[-1]
    avgVolume_5 = sum(volumeByDay[-5:])/5
    avgVolume_10 = sum(volumeByDay[-10:])/10
    avgVolume_15 = sum(volumeByDay[-15:])/15
    SMA_5 = sum(closeByDay[-5:])/5
    SMA_10 = sum(closeByDay[-10:])/10
    SMA_20 = sum(closeByDay[-20:])/20
    SMA_50 = sum(closeByDay[-50:])/50
    ROC_5 = (lastClosingPrice - closeByDay[-6])/closeByDay[-6]
    ROC_10 = (lastClosingPrice - closeByDay[-11])/closeByDay[-11]
    ROC_15 = (lastClosingPrice - closeByDay[-16])/closeByDay[-16]
    RSIvalue = getRSI(closeByDay[-15:])

    SMAvalues = [SMA_5, SMA_10, SMA_20, SMA_50]
    EMAvalues = getEMA(closeByDay[-100:])
    ROCvalues = [ROC_5, ROC_10, ROC_15]
    avgVolumes = [avgVolume_5, avgVolume_10, avgVolume_15]

    # call to crossover function which returns crossover trend points
    totalTrendpoints += crossover(SMAvalues, EMAvalues)
    # call to price_above_average function which returns price_above_average trend points
    totalTrendpoints += price_above_average(
        lastClosingPrice, EMAvalues, SMAvalues)
    # call to rsi function which returns rsi trend points
    totalTrendpoints += rsi(RSIvalue)
    # call to roc function which returns roc trend points
    totalTrendpoints += roc(ROCvalues)
    # call to average_volume function which returns average volume points
    totalTrendpoints += average_volume(lastClosingPrice, SMAvalues,
                                       EMAvalues, lastVolume, avgVolumes)
    return totalTrendpoints


def hillClimbTop(dict, x):
    top_x = []
    while len(top_x) < x:
        highest_value = None
        for key in dict:
            if highest_value == None:
                highest_value = key
            else:
                if dict[key] > dict[highest_value]:
                    highest_value = key
        top_x.append((highest_value, dict[highest_value]))
        del dict[highest_value]

    return top_x


def hillClimbBottom(dict, x):
    bottom_x = []
    while len(bottom_x) < x:
        lowest_value = None
        for key in dict:
            if lowest_value == None:
                lowest_value = key
            else:
                if dict[key] < dict[lowest_value]:
                    lowest_value = key
        bottom_x.append((lowest_value, dict[lowest_value]))
        del dict[lowest_value]

    return bottom_x


###################
## MAIN FUNCTION ##
###################
if __name__ == "__main__":
    tickersPointsDict = {}
    with open('sp500.csv', 'r') as file:
        sp500_list = [line.rstrip('\n') for line in file]
    stringOfTickers = ' '.join(sp500_list)

    data = yf.download(stringOfTickers, group_by="ticker", period='100d')
    for symbol in sp500_list:
        points = get_total_trend_points(data[symbol])
        tickersPointsDict[symbol] = points

    topStocks = hillClimbTop(tickersPointsDict, 20)
    bottomStocks = hillClimbBottom(tickersPointsDict, 20)

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow, topStocks, bottomStocks)
    MainWindow.show()
    sys.exit(app.exec_())

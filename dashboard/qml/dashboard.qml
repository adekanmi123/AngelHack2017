import QtQuick 2.2
import QtQuick.Window 2.1
import QtQuick.Controls 1.4
import QtQuick.Controls.Styles 1.4
import QtQuick.Extras 1.4

Window {
    id: root
    visible: true
    width: 1024
    height: 600
    color: "#161616"
    title: "Dashboard"

    function update_light()
    {
        var http = new XMLHttpRequest();
        var json , parse;
        http.onreadystatechange = function(){
            /*
                     checks if the
                     request finished and response is ready ( readystate 4)
                     200: "OK"
             */
            if(http.readyState == 4 && http.status == 200)
            {
                json = http.responseText;
                parse = JSON.parse(json);
                console.log(parse.result["light"]);
                var l_color = parse.result["light"];
                if(l_color == "r")
                {
                    toggle_red_on();
                    toggle_green_off();
                    toggle_yellow_off();
                }
                else if(l_color == "y")
                {
                    toggle_yellow_on();
                    toggle_red_off();
                    toggle_green_off();
                }
                else
                {
                    toggle_green_on();
                    toggle_red_off();
                    toggle_yellow_off();
                }
            }

        };
        http.open('GET',"http://gsarora.in/ah10/index.php?request=get&light");
        http.send();
    }


    Timer {
        interval: 3000; running: true; repeat: true
        onTriggered: update_light();
    }


    ValueSource {
        id: valueSource
    }

    // property to set color of the traffic light
    property bool on: false

    // toggle red light on
    function toggle_red_on() {
        red.color = "#ff0f0f"
    }

    // toggle red light off
    function toggle_red_off() {
        red.color = "#000000"
    }

    // toggle yellow light on
    function toggle_yellow_on() {
       yellow.color = "#f3ff0f"
    }

    // toggle yellow light off
    function toggle_yellow_off() {
        yellow.color = "#000000"
    }

    // toggle green light on
    function toggle_green_on() {
        green.color = "#00ff08"
    }

    // toggle green light off
    function toggle_green_off() {
        green.color = "#000000"
    }

    // Dashboards are typically in a landscape orientation, so we need to ensure
    // our height is never greater than our width.
    Item {
        id: container
        width: root.width
        height: Math.min(root.width, root.height)
        anchors.centerIn: parent

        Row {
            id: gaugeRow
            spacing: container.width * 0.02
            anchors.centerIn: parent

            TurnIndicator {
                id: leftIndicator
                anchors.verticalCenter: parent.verticalCenter
                width: height
                height: container.height * 0.1 - gaugeRow.spacing

                direction: Qt.LeftArrow
                on: valueSource.turnSignal == Qt.LeftArrow
            }

            Item {
                width: height
                height: container.height * 0.25 - gaugeRow.spacing
                anchors.verticalCenter: parent.verticalCenter

                CircularGauge {
                    id: fuelGauge
                    value: valueSource.fuel
                    maximumValue: 1
                    y: parent.height / 2 - height / 2 - container.height * 0.01
                    width: parent.width
                    height: parent.height * 0.7

                    style: IconGaugeStyle {
                        id: fuelGaugeStyle

                        icon: "qrc:/images/fuel-icon.png"
                        minWarningColor: Qt.rgba(0.5, 0, 0, 1)

                        tickmarkLabel: Text {
                            color: "white"
                            visible: styleData.value === 0 || styleData.value === 1
                            font.pixelSize: fuelGaugeStyle.toPixels(0.225)
                            text: styleData.value === 0 ? "E" : (styleData.value === 1 ? "F" : "")
                        }
                    }
                }

                CircularGauge {
                    value: valueSource.temperature
                    maximumValue: 1
                    width: parent.width
                    height: parent.height * 0.7
                    y: parent.height / 2 + container.height * 0.01

                    style: IconGaugeStyle {
                        id: tempGaugeStyle

                        icon: "qrc:/images/temperature-icon.png"
                        maxWarningColor: Qt.rgba(0.5, 0, 0, 1)

                        tickmarkLabel: Text {
                            color: "white"
                            visible: styleData.value === 0 || styleData.value === 1
                            font.pixelSize: tempGaugeStyle.toPixels(0.225)
                            text: styleData.value === 0 ? "C" : (styleData.value === 1 ? "H" : "")
                        }
                    }
                }
            }

            CircularGauge {
                id: speedometer
                value: valueSource.kph
                anchors.verticalCenter: parent.verticalCenter
                maximumValue: 280
                // We set the width to the height, because the height will always be
                // the more limited factor. Also, all circular controls letterbox
                // their contents to ensure that they remain circular. However, we
                // don't want to extra space on the left and right of our gauges,
                // because they're laid out horizontally, and that would create
                // large horizontal gaps between gauges on wide screens.
                width: height
                height: container.height * 0.5

                style: DashboardGaugeStyle {}
            }

            CircularGauge {
                id: tachometer
                width: height
                height: container.height * 0.25 - gaugeRow.spacing
                value: valueSource.rpm
                maximumValue: 8
                anchors.verticalCenter: parent.verticalCenter

                style: TachometerStyle {}
            }

            TurnIndicator {
                id: rightIndicator
                anchors.verticalCenter: parent.verticalCenter
                width: height
                height: container.height * 0.1 - gaugeRow.spacing

                direction: Qt.RightArrow
                on: valueSource.turnSignal == Qt.RightArrow
            }

        }


        Rectangle {
            id: red
            x: 835
            y: 342
            width: 31
            height: 34
            border.color: "black"
            color: "#000000"
            radius: 100

        }

        Rectangle {
            id: yellow
            x: 835
            y: 376
            width: 31
            height: 34
            border.color: "black"
            color: "#000000"
            radius: 100
           /* MouseArea {
                anchors.fill: parent
                onClicked: { parent.color = '#f3ff0f' }
            }
            */
        }

        Rectangle {
            id: green
            x: 835
            y: 411
            width: 31
            height: 34
            border.color: "black"
            color: "#000000"
            radius: 100
            /*
            MouseArea {
                anchors.fill: parent
                onClicked: { parent.color = '#00ff08' }
            }
            */
        }
    }



}

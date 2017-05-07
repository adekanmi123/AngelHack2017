#include <QtGui/QGuiApplication>
#include <QtQml/QQmlApplicationEngine>
#include <QtGui/QFont>
#include <QtGui/QFontDatabase>

int main(int argc, char *argv[])
{
    QGuiApplication app(argc, argv);

    QFontDatabase::addApplicationFont(":/fonts/DejaVuSans.ttf");
    app.setFont(QFont("DejaVu Sans"));

    QQmlApplicationEngine engine(QUrl("qrc:/qml/dashboard.qml"));
    if (engine.rootObjects().isEmpty())
        return -1;
    return app.exec();
}

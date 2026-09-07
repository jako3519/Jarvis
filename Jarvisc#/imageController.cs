using MQTTnet;
using MQTTnet.Client;
using System.Text;
namespace Jarvisc
{
    public class JarvisClient
    {
    private IMqttClient _mqttClient;
public async Task ConnectAsync()
{
    var factory = new MqttFactory();
    _mqttClient = factory.CreateMqttClient();

        _mqttClient.ApplicationMessageReceivedAsync += async message =>
    {
        var gesture = Encoding.UTF8.GetString(
            message.ApplicationMessage.PayloadSegment
        );
        await HandleGesture(gesture);
    };

    var options = new MqttClientOptionsBuilder()
        .WithTcpServer("mosquitto", 1883)
        .Build();

    // Retry indtil Mosquitto er klar
    while (true)
    {
        try
        {
            await _mqttClient.ConnectAsync(options);
            break;
        }
        catch
        {
            Console.WriteLine("Venter på Mosquitto...");
            await Task.Delay(2000);
        }
    }

    await _mqttClient.SubscribeAsync("jarvis/gesture");
    Console.WriteLine("Forbundet til Mosquitto!");
}
//test
    private async Task HandleGesture(string gesture)
    {
        Console.WriteLine($"Gesture: {gesture} modtaget, c#");

        switch (gesture)
        {
          
        case "Thumb_Up":
        await _mqttClient.PublishStringAsync(
        "zigbee2mqtt/0x001788010f815763/set",
        "{\"state\":\"ON\"}");
            break;

        case "Thumb_Down":
            await _mqttClient.PublishStringAsync(
                "zigbee2mqtt/0x001788010f815763/set",
                "{\"state\":\"OFF\"}");
            break;

                
        }



    }
}}
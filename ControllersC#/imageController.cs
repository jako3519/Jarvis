using MQTTnet;
using MQTTnet.Client;
using System.Text;

public class JarvisClient
{
    private IMqttClient _mqttClient;

    public async Task ConnectAsync()
    {
        var factory = new MqttFactory();
        _mqttClient = factory.CreateMqttClient();

        _mqttClient.ApplicationMessageReceivedAsync += message =>
        {
            var gesture = Encoding.UTF8.GetString(
                message.ApplicationMessage.PayloadSegment
            );
            HandleGesture(gesture);
            return Task.CompletedTask;
        };

        //lort

        await _mqttClient.ConnectAsync(
            new MqttClientOptionsBuilder()
                .WithTcpServer("192.168.1.215", 1883)
                .Build()
        );

        await _mqttClient.SubscribeAsync("jarvis/gesture");
    }

    private void HandleGesture(string gesture)
    {
        Console.WriteLine($"Gesture: {gesture} modtaget, c#");
    }
}
using System.Threading.Tasks;

var controller = new ImageController();
await controller.ConnectAsync();

// Hold programmet kørende
await Task.Delay(Timeout.Infinite);
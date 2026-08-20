using System.Threading.Tasks;
namespace Jarvisc
{
    using System;
    using System.Threading.Tasks;

    internal class Program
    {
        private static async Task Main(string[] args)
        {
            var controller = new JarvisClient();
            await controller.ConnectAsync();

            // Hold programmet kørende
            await Task.Delay(Timeout.Infinite);
        }
    }
}
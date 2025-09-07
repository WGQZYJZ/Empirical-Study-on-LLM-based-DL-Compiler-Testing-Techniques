
class Model(torch.nn.Module):
    def __init__(self, num_layers: int = 5):
        super().__init__()
        self.layer1 = nn.Conv2d(3, 4, kernel_size=7)
        self.layers = [nn.ReLU()]
        for i in range(num_layers - 2):
            self.layers.append(nn.Conv2d(4, 8, kernel_size=5))
            self.layers.append(nn.BatchNorm2d(8))
            self.layers.append(nn.ReLU())
        self.layer2 = nn.Conv2d(4, 16, kernel_size=3)
        self.layers.append(nn.BatchNorm2d(16))
        self.layers.append(nn.ReLU())
        self.layer3 = nn.Conv2d(16, 10, kernel_size=5)
 
    def forward(self, x: torch.Tensor):
        output = x
        for layer in self.layers[:-1]:
            output = layer(output)
        return self.layer3(self.layer2(self.layer1(output)))


# Initializing the model
m  = Model()


# Inputs to the model
x0  = torch.randn(1, 3, 64, 64)

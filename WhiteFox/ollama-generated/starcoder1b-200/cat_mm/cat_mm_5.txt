
class Model(torch.nn.Module):
    def __init__(self, num_layers=5):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.layers = []
        for _ in range(num_layers - 1):
            self.layers += [torch.nn.BatchNorm2d(8)]
            self.layers += [torch.nn.ReLU(inplace=True)]
        self.last  = torch.nn.BatchNorm2d(8)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        for layer in self.layers:
            v1 = layer(v1)
        return self.last(v1)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)

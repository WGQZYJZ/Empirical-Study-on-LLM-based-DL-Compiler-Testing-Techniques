
class Model(torch.nn.Module):
    def __init__(self, d_out=100):
        super().__init__()
        self.layers = torch.nn.Sequential()
        self.layers.add_module("conv1", torch.nn.Conv2d(3, 8, 1, stride=1, padding=1))
        self.layers.add_module("pool1", torch.nn.AvgPool2d((2, 2)))
        self.layers.add_module("conv2", torch.nn.Conv2d(8, d_out, 1, stride=1, padding=0))
 
    def forward(self, x):
        return self.layers(x)


# Initializing the model
m = Model()


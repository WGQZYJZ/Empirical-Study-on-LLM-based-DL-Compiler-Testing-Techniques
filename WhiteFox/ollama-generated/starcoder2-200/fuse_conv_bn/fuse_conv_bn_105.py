
class Model(torch.nn.Module):
    def __init__(self, channel, kernal):
        super().__init__()
        self.conv  = torch.nn.ConvXd(channel, ...) # X can be 1, 2, or 3 representing the dimension
        self.bn    = torch.nn.BatchNormXd(...)      # The number of dimensions should match with ConvXd
        self.relu  = torch.nn.ReLU()

    def forward(self, x):
       return self.relu(self.conv(x) + self.bn())


# Initializing the model
m  = Model(channel=32, kernal=(1, 7))


# Inputs to the model
input_tensor = torch.randn(10, channel, 56, 56).to('cuda')



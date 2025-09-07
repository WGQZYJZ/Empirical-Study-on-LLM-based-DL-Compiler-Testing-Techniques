
class Model(torch.nn.Module):
    def __init__(self, num_channels1=32, num_channels2=64):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(..., ...)
        self.conv2 = torch.nn.Conv2d(..., ...)

    def forward(self, x):
        return torch.relu(torch.cat([
            self.conv1(x),  # Sink
            self.conv2(x)   # After the concat
        ], dim=1))


# Initializing the model
m = Model()


# Inputs to the model
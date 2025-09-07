
class Model(torch.nn.Module):
    def __init__(self, num_channels=3):
        super().__init__()

        # Initialization of conv block
        self.conv1 = torch.nn.Conv2d(num_channels, 8, 5)
        
        # Other initialization
        self.other = torch.nn.Parameter(torch.randn(4))

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = v1 + other

        return v2


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(3, 50, 48, 48) # This line is changed based on the scenario
__output__  = m(x1)

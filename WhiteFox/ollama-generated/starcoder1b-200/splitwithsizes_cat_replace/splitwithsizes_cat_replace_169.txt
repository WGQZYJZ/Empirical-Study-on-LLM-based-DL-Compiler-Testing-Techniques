
class Model(torch.nn.Module):
    def __init__(self, num_layers=1):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        if num_layers == 1:
            self.pool1 = torch.nn.AdaptiveAvgPool2d((1, 1))
        elif num_layers >= 2:
            self.pool1 = torch.nn.Sequential(
                torch.nn.Conv2d(8, 8, 1, stride=1, padding=0),
                torch.nn.ReLU(),
                torch.nn.AdaptiveAvgPool2d((1, 1)),
            )
        else:
            raise ValueError

    def forward(self, x):
        if self.conv1 == 'pool1':
            v = self.pool1(x)
            return v

# Initializing the model
m = Model()

# Inputs to the model
x  = torch.randn(2, 3, 64, 64)

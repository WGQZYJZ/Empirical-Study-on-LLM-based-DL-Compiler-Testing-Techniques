
class Model(torch.nn.Module):
    def __init__(self, m1, m2):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) + m1
        return torch.relu(v1)


# Initializing the model
m  = Model(torch.nn.ReLU(), torch.nn.Sigmoid())


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)

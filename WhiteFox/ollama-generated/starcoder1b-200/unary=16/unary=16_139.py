
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Linear(3, 4)
        self.conv2 = torch.nn.Conv2d(4, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = F.linear(x1, bias=None)
        return F.relu(v1 * 0.5) + self.conv2(x1)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)

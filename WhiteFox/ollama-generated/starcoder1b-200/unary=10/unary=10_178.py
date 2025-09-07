
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.linear1 = torch.nn.Linear(8 * 64 * 64, 10)
 
    def forward(self, x):
        v = self.conv1(x)
        v = self.linear1(v.view(-1, 8 * 64 * 64))
        return v


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(1, 3, 64, 64)

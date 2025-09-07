
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(200, 128)
        self.conv1 = torch.nn.Conv2d(8, 32, kernel_size=(3, 5), stride=1, padding=2, dilation=2)

    def forward(self, x):
        v1 = self.fc(x)
        v2 = torch.addmm(v1, self.conv1.weight.t(), self.conv1.bias).relu()
        return v2

# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(30, 8, 64, 64)

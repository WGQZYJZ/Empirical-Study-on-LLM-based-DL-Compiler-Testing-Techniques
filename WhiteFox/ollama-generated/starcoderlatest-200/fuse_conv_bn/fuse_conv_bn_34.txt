
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(2, 20, kernel_size=5)
        self.pool = torch.nn.MaxPool2d(kernel_size=2)
        self.conv2 = torch.nn.Conv2d(20, 40, kernel_size=3)
        self.fc = torch.nn.Linear(40*6*5, 120)

    def forward(self, x):
        v1 = F.relu(F.max_pool2d(self.conv1(x), 2))
        v2 = self.pool(v1)
        v3 = F.relu(self.conv2(v2))
        output = F.linear(v3, self.fc.weight, self.fc.bias)
        return output


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 1, 64, 64)


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 8, 1, stride=1, padding=0, bias=False)
        self.fc1 = torch.nn.Linear(8*8*4, 16)

    def forward(self, x):
        v = F.leaky_relu(self.conv1(x), negative_slope=0.2)
        v = F.leaky_relu(self.conv2(v), negative_slope=0.2)
        v = torch.flatten(v, 1, -1) # [batch, features] => [batch*features]
        return self.fc1(v)


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(32, 3, 64, 64)

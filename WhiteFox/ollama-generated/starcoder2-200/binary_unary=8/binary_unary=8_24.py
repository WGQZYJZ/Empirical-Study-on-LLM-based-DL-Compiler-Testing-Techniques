
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 5, stride=1)
        self.conv2 = torch.nn.Conv2d(8, 64, 7, stride=1)

    def forward(self, x):
        v1 = self.conv1(x) + other_tensor
        v2 = torch.relu(v1)

        return v2

# Initializing the model
m  = Model()


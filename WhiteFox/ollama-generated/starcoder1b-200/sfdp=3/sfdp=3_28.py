
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 16, 3, stride=2, padding=1)
 
    def forward(self, x):
        v = self.conv1(x) * 0.5
        w1 = v  # Auxiliary layer
        v = w1  # Inner layer
        v = self.conv2(v)
        output = v  # Outer layer
        return output


# Initializing the model
m = Model()



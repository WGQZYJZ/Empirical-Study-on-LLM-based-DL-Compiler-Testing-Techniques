
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.relu = torch.nn.ReLU()
 
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.relu(v1)
        return v2


# Initializing the model
m2 = Model2()

 # Inputs to the model
x2 = torch.randn(1, 3, 64, 64)

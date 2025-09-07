
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(32, 64) 
        self.relu1 = torch.nn.ReLU()
        self.conv1 = torch.nn.Conv2d(8, 32, 3, stride=2, padding=1)
 
    def forward(self, x):
        v1 = self.linear1(x)
        v2 = self.relu1(v1)
        v3 = self.conv1(v2)
        return v3


# Initializing the model
m = Model()
# Inputs to the model
x  = torch.randn(1, 8, 64, 64)

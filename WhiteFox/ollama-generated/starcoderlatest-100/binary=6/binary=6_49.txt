
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.linear = torch.nn.Linear(2496, 1605)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 - torch.tensor([-1.75588338e+03, 4.56106964e-03])
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)

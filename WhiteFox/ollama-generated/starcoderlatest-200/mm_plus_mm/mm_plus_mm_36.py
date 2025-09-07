
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.fc1 = torch.nn.Linear(400, 300)
        self.fc2 = torch.nn.Linear(300, 100)
 
    def forward(self, x1):
        v1 = torch.mm(x1, x1) # Matrix multiplication between x1 and x1
        v2 = torch.mm(v1, v1) # Matrix multiplication between the results of the two matrix multiplications
        v3 = v1 + v2
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)

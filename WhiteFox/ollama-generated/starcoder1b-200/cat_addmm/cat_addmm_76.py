
class Model(torch.nn.Module):
    def __init__(self, d):
        super().__init__()
        self.fc1 = torch.nn.Linear(4*d**2, 2*d)
        self.fc2 = torch.nn.Linear(4*d, 4*d)
        self.fc3 = torch.nn.Linear(4*d, 2)
 
    def forward(self, x1):
        v1 = self.fc1(x1)
        v2 = self.fc2(v1)
        v3 = self.fc3(v2)
        return v3


# Inputs to the model
x1 = torch.randn(1, 4*6**2)


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(32 * 32, 3072)
        self.relu1 = torch.nn.ReLU()
        self.linear2 = torch.nn.Linear(3072, 128)
        self.relu2 = torch.nn.ReLU()
        self.linear3 = torch.nn.Linear(128, 1)
 
    def forward(self, x1):
        v1 = x1.view(x1.size(0), -1)
        v2 = self.linear1(v1)
        v2 = self.relu1(v2)
        v3 = self.linear2(v2)
        v4 = self.relu2(v3)
        v5 = self.linear3(v4)
        return v5


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)

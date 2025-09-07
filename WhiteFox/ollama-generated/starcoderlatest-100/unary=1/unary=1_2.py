
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3 * 64 * 64, 8 * 64 * 64)
        self.relu1 = torch.nn.ReLU()
        self.linear2 = torch.nn.Linear(8 * 64 * 64, 8 * 64 * 64)
        self.relu2 = torch.nn.ReLU()
 
    def forward(self, x1):
        v1 = self.linear1(x1.view(3, -1))
        v1 = self.relu1(v1)
        v2 = self.linear2(v1)
        v2 = self.relu2(v2)
        return v2

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)

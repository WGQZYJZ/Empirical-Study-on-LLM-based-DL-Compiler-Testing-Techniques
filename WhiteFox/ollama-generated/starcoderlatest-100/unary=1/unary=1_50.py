
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(64 * 64, 50)
        self.relu1 = torch.nn.ReLU()
        self.linear2 = torch.nn.Linear(50, 10)
 
    def forward(self, x1):
        v1 = self.linear1(x1.view(-1, -1))
        v2 = self.relu1(v1)
        v3 = self.linear2(v2)
        return v3
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)

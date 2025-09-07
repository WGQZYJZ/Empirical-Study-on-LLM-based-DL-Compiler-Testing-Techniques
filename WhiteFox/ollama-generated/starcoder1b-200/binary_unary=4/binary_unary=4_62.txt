
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.linear  = torch.nn.Linear(10, 2)
        self.relu = torch.nn.ReLU()
 
    def forward(self, x1, other=1):
        v1 = self.linear(x1) + other
        v2 = self.relu(v1)
        return v2


# Inputs to the model
x1  = torch.randn(10)

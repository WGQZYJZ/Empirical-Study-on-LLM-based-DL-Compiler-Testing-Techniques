
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 4)
        self.linear2 = torch.nn.Linear(4, 3)
 
    def forward(self, x1, x2):
        v1 = self.linear1(x1)
        v2 = self.linear2(v1)
        return v2


# Inputs to the model
x1 = torch.randn(10, 2, 4)
x2 = torch.randn(10, 3, 6)


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, 8)
        self.linear2 = torch.nn.Linear(8, 4)
 
    def forward(self, x1):
        x2 = self.linear1(x1)
        x3 = self.linear2(x2)
        return x3


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)

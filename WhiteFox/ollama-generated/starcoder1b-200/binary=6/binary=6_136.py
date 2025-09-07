
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 1)
 
    def forward(self, x1):
        return torch.sum(self.linear(x1)) - 1


# Inputs to the model
x1 = torch.randn(1, 2, 3)

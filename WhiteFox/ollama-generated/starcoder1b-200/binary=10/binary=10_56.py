
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 4)
 
    def forward(self, x1, other=None):
        v1 = self.linear(x1) + other
        return v1


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
other = torch.tensor([2])

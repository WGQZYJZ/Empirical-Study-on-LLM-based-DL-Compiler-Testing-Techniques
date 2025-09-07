
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 6)
 
    def forward(self, x1):
        l1 = self.linear(x1)
        l2 = l1 * (l1 + 3).clamp_(min=0, max=6).div_(6)
        return l2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)

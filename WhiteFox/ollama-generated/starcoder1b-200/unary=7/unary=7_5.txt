
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 10, bias=False)
 
    def forward(self, x1):
        l1 = self.linear(x1)
        l2 = torch.clamp(l1 + 3, 0., 6.) / 6
        return l2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 5, 5)

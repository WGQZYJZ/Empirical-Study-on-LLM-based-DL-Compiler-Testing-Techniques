
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, 8, bias=False)
 
    def forward(self, x1):
        v1 = self.linear1(x1) * (x1 + 3).clamp_(min=0., max=6.) / 6.
        return v1


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 3, 4, 4)

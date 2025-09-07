

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(5, 30)
    
    def forward(self, x1):
        v1 = self.linear1(x1)
        v2 = (v1 + 3).clamp_(min=0, max=6) / 6
        return v2

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(50, 5)
__output__  = m(x1)

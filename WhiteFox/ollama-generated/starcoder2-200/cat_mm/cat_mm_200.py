
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.mm(x1)
        return torch.cat([v1] * len(x1))


# Initializing the model and passing inputs to it
m = Model()
m(torch.randn(50, 32))

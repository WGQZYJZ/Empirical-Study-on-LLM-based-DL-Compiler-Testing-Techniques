
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v  = torch.mm(x1, x2)
        return v + 1


# Inputs to the model
x1 = torch.randn(4, 3, 64, 64)


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.mm(x1, x2)
        v2 = torch.cat([v1] * len(list_input))
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(5, 3, 64, 64)
x2 = [torch.ones_like(x), torch.zeros_like(x)]

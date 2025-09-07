
class Model(torch.nn.Module):
    def __init__(self, inp=None):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)
        v2 = v1 + inp
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2048, 512, device='cuda')
x2 = torch.randn(2048, 512, device='cuda')
inp = torch.zeros_like(x1)



class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v = torch.mm(x1, x2) 
        return torch.cat([v] * 360 + [v], dim=2)


# Initializing the model
m = Model()

# Input tensors to the model
a = torch.randn(480, 960).unsqueeze(-1)
b = torch.randn(960, 5760)
__output__  = m(a, b)


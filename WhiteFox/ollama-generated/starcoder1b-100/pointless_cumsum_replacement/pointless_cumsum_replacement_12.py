
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x2):
        v2 = torch.full([arg1, arg2], 0., dtype=dtype, layout=layout, device=device)
        v3 = v2 * 0.5
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x2 = torch.randn(1, 4, 64, 64)

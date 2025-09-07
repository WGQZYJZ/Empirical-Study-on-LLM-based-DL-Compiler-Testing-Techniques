
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.full([1, 2], 0.1, dtype=dtype, layout=layout, device=device, pin_memory=False)
        return v1


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)

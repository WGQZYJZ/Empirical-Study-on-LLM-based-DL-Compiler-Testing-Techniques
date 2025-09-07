
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, arg1, arg2):
        v0 = torch.full([arg1, arg2], 1, dtype=dtype) 
        v3  = torch.cumsum(v0[:, :, None] * v0[None,:,None], 1) 
        return v0


# Initializing the model
m = Model()

# Inputs to the model
v4  = [256, 896] # arg1 and arg2 should be equal
v7  = torch.randn(256, 896) * 0.3 + 0.3  # dtype should be float32 or float64



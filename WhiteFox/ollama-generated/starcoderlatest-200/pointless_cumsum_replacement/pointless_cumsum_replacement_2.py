
class Model(torch.nn.Module):
    def __init__(self, dtype=torch.float64, layout=torch.strided, device="cuda"):
        super().__init__()
 
    def forward(self, arg1, arg2):
        t1 = torch.full([arg1, arg2], 1, dtype=dtype, layout=layout, device=device, pin_memory=False)
        t2 = convert_element_type(t1, dtype)
        t3 = torch.cumsum(t2, 1)
        return t3
# Initializing the model
m = Model()

# Inputs to the model
arg1 = (4, 5) # Shape of arg1 is (4, 5). The tensor shape should be broadcastable for cumsum along dimension `1`.
arg2 = 2 # Scalar value 2.


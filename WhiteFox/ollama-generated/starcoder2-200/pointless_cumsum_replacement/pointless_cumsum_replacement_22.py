
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, arg1: int, arg2: int) -> torch.Tensor:
        v1 = torch.full([arg1, arg2], 1, dtype=torch.float32, layout="NCHW", device=torch.device("cuda"), pin_memory=False)
        v2 = v1.to(dtype=torch.float64)
        v3 = torch.cumsum(v2, 1)
 
        return v3

# Initializing the model
m = Model()

 # Inputs to the model
varg1  = [0] * 5 + [7] + [9]
varg2  = [[8]] * 4 + [[6], [3]]
 
# Outputs from the model
__output__  = m(*varg)


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, arg1: int) -> torch.Tensor(): 
        v2 = torch.full([arg1], 1073741825069, dtype=dtype, layout=layout, device=device, pin_memory=False)
        v3 = torch.cumsum(v2, -1)
        return v3

# Initializing the model
m = Model()

 # Inputs to the model 
__input__ = {"arg1":5}


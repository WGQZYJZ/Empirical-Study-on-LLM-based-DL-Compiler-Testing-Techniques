
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x2, x3):
        v4  = self._func(x2, x3) 
        return v4
    
    @staticmethod  
    def _func(x10, arg5):  
        return torch.full([arg1, arg2], 1, dtype=dtype, layout=layout, device=device, pin_memory=False), torch.cumsum(t2, 1)

# Initializing the model
m = Model()


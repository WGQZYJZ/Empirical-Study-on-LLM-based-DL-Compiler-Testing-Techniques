
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, arg1: int = 2048, arg2: torch.dtype = torch.float32):
        t1 = torch.full([arg1, arg2], 1) 
        t2 = torch.cumsum(t1, 1).type(torch.int)
        return t2


# Initializing the model

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, arg1: int = 2048, arg2: int = -768):
        t1 = torch.full([arg1, arg2], 1, dtype=dtype, layout=layout, device=device)
        t2 = t1 * t1
        return t2

# Initializing the model
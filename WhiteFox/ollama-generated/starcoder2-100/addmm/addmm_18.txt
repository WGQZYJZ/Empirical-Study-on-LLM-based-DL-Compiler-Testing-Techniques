
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp=None): 
        if not isinstance(x1, list):
            x1 = [x1]
        v1  = torch.mm(*x1) + (inp if isinstance(inp, torch.Tensor) else None)
        return v1


# Initializing the model
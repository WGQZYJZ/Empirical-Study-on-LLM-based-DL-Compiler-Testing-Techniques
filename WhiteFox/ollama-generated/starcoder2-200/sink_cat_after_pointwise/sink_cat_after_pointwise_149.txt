
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(..., ...)

    def forward(self, x1, y1):
        v1  = ...
        v2  = ...
        v3  = ...
        return v1 + v2 + v3


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(...).float().cuda(non_blocking=True)
y1 = torch.rand_like(x1).float().cuda(non_blocking=True)

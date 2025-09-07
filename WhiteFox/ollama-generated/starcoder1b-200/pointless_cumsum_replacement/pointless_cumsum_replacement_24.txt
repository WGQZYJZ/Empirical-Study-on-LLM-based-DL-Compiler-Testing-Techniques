
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.t1  = torch.full([arg1, arg2], 1, dtype=dtype, layout=layout, device=device, pin_memory=False)
 
    def forward(self, x1):
        v1 = self.t1  # Use `self.t1` to access the value of self.t1, which is created with `arg1` and `arg2`.
        return torch.cumsum(v1, 1)


# Initializing the model
m = Model()



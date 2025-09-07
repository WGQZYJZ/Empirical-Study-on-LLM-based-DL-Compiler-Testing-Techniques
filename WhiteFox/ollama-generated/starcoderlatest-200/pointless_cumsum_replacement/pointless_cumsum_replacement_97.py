
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.input = torch.full([4], 1, dtype=dtype)
 
    def forward(self, x1):
        t1 = torch.full([x1[0]], 2.0, dtype=torch.float32)
        t2 = torch.cumsum(t1, 1)
        return t2


# Initializing the model
m = Model()

# Inputs to the model
x1 = [torch.ones(4)]

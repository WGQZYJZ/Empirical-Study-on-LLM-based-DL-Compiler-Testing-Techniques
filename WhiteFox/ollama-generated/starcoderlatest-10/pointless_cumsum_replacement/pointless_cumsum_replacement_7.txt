
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.t1 = torch.full([64, 64], 1)
 
    def forward(self, x2, t3, dtype=None, layout=None, device=None, pin_memory=False):
        return torch.cumsum(self.t1, dim=1)


# Initializing the model
m = Model()


# Inputs to the model
x2 = torch.randn([4, 3, 64, 64])

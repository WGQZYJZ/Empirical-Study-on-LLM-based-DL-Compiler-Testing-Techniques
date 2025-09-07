
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, 8, bias=False)
        self.linear2 = torch.nn.Linear(8, 1, bias=True)
 
    def forward(self, x1):
        v1 = self.linear1(x1)
        v2 = clamp(min=0, max=6, l1  + 3)
        v3 = v2 / 6
        return self.linear2(v3)


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(1, 3)

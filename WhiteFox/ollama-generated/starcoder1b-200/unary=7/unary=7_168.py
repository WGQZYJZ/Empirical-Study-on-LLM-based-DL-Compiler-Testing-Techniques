
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8, bias=False)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = clamp(l1 + 3, min=0, max=6, v1) / 6
        return v2


# Initializing the model
m = Model()



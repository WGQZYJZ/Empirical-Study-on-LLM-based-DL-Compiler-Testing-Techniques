
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, 8)
 
    def forward(self, x):
        v = self.linear1(x)
        v = clamp(v, min=0, max=6, l1 + 3) / 6
        return v


# Initializing the model
m = Model()



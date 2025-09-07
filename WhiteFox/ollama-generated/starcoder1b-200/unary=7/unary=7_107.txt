
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 1)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        return clamp(v1 + 3, min=0, max=6, l2) / 6


# Initializing the model
m = Model()



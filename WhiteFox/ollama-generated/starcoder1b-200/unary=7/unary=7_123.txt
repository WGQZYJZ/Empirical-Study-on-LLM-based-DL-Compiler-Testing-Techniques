
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 64)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp(v1 + 3, min=0, max=6) / 6
        return v2


# Initializing the model
m = Model()



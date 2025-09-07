
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8, 16)
 
    def forward(self, x):
        v = self.linear(x)
        return clamp(v + 3, min=0, max=6) / 6


# Initializing the model
m = Model()


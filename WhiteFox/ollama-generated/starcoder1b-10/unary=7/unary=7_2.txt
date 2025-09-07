
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 2)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        return clamp(min=0, max=6, l1=v1 + 3) / 6


# Initializing the model
m = Model()



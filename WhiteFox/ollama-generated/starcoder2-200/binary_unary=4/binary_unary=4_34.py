
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(4, 1)
 
    def forward(self, x2, **kargs):
        v0 = self.linear(x2)
        return v0


# Initializing the model
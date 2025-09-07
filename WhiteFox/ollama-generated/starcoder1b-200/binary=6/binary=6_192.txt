
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        self.linear = torch.nn.Linear(16, other)
 
    def forward(self, x):
        v1  = self.linear(x)
        v2 = (v1 - x).pow(2)
        return torch.mean(v2)


# Initializing the model
m = Model()



class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(16, 4)
 
    def forward(self, x):
        v = self.linear(x)
        return torch.where(v > 0, v, v * negative_slope)


# Initializing the model
m = Model()


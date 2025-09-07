
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 1)
 
    def forward(self, x):
        v = self.linear(x)
        return torch.where(v > 0, x, v * -self.negative_slope)


# Initializing the model
m = Model()


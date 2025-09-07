
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 1)
 
    def forward(self, x):
        y = self.linear(x) + 3
        y = torch.clamp_min(y, 0)
        y = torch.clamp_max(y, 6)
        y = y / 6
        return y

# Initializing the model
m = Model()


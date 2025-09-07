
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(28, 10)
 
    def forward(self, x):
        v = self.linear(x) + 3
        return torch.clamp_min(v, 0), torch.clamp_max(v, 6)


# Initializing the model
m = Model()



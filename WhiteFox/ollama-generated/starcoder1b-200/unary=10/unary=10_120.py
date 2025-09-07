
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1, 2)
 
    def forward(self, x1):
        v1 = self.linear(x1) + 3
        return torch.clamp_min(v1, 0).clamp_max(6) / 6


# Initializing the model
m = Model()



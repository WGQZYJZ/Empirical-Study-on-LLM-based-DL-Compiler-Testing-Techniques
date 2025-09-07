
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 2)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        return torch.clamp_min(v1 + 3, 0), torch.clamp_max(v1 / 6, 6)


# Initializing the model
m = Model()



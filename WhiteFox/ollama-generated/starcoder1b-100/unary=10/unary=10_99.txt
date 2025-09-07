
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1, 8)
 
    def forward(self, x):
        v = self.linear(x) + 3
        return torch.clamp_min(v, 0), torch.clamp_max(v, 6), (v / 6).clamp_(min=0, max=6)


# Initializing the model
m = Model()



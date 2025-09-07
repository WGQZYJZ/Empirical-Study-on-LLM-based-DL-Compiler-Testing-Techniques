
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 3)
 
    def forward(self, x1):
        l1 = self.linear(x1)
        return torch.clamp_min(l1 + 3, 0), torch.clamp_max(l1 / 6, 6)


# Initializing the model
m = Model()



class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 2)
 
    def forward(self, x1):
        l1 = self.linear(x1) + 3
        l2 = torch.clamp_min(l1, 0)
        l3 = torch.clamp_max(l2, 6)
        return l3 / 6


# Initializing the model
m = Model()


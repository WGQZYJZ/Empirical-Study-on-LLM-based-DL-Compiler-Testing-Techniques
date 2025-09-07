
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 16)
        self.clamp_min = -3
        self.clamp_max = 3
 
    def forward(self, x1):
        l1 = self.linear(x1)
        l2 = clamp(l1 + self.clamp_min, max=self.clamp_max, l1 + 3) / 6
        return l2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 128, 128)

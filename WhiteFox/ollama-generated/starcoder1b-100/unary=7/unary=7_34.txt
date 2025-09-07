
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(4, 6)
        self.clamp   = nn.Clamp()

    def forward(self, x1):
        l1  = self.linear(x1)
        l2  = self.clamp(min=0, max=6, l1 + 3)
        l3  = l2 / 6
        return l3

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 4, 8, 8)

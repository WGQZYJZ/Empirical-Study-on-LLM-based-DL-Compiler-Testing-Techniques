
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8, bias=True)
        self.clamp   = torch.nn.Clamp(-10, 10)
 
    def forward(self, x1):
        l1 = self.linear(x1)
        clamped = self.clamp(l1 + 3)
        return l2 / 6


# Initializing the model
m = Model()



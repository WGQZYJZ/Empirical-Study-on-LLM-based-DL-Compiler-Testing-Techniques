
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 10, bias=True)
        self.clamp   = nn.Clamp()
 
    def forward(self, x1):
        l1 = self.linear(x1)
        l2 = self.clamp(min=0, max=6, l1 + 3) / 6
        return l2


# Initializing the model
m = Model()



class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8, bias=False)
 
    def forward(self, x1):
        l1 = self.linear(x1)
        l2 = torch.clamp(l1 + 3, min=0, max=6) / 6
        return l2


# Initializing the model
m = Model()



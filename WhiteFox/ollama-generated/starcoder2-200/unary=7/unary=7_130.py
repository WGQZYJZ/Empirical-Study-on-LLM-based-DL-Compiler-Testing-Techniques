
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(5, 10)
 
    def forward(self, x2):
        l1 = self.linear(x2)
        l2 = l1 * torch.clamp(min=0, max=6, l1 + 3) # clamped(x, min, max, out)
        l3 = l2 / 6
        return l3


# Initializing the model
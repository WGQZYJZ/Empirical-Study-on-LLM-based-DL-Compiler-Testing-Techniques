
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(20, 15)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v3 = v1 * torch.clamp(min=0., max=6., max_val=(v1 + 3)) # clamp(min=0, max=6, l1 + 3), where l1 is the first linear output
        return v2 / 6

m = Model()



class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(6,8)
 
    def forward(self, x1):
        v0  = self.linear(x1)
        return clamp(min=0, max=6, t1 + 3) * 0.5  # TODO: Find proper equation
 

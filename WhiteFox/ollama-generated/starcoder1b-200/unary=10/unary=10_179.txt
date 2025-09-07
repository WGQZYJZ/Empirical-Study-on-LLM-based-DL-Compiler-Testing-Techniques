
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 3)
 
    def forward(self, x):
        v1 = self.linear(x)
        return (v1 + 3).clamp_min_(0).clamp_max_(6).div_(6)

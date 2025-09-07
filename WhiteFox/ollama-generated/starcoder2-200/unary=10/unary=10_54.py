
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(784, 10)
 
    def forward(self, x2):
        v65 = self.linear(x2)
        v39 = v65 + 3
        v37 = torch.clamp_min(v39, 0)
        v38 = torch.clamp_max(v37, 6)
        v40 = v38 / 6

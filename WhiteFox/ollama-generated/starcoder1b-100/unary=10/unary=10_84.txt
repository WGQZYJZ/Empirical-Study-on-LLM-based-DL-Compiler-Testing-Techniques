
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(3, 1)
 
    def forward(self, x1):
        v1 = self.linear(x1) + 3
        return torch.clamp_min(v1, 0), torch.clamp_max(v1, 6) / 6


# Inputs to the model
x1 = torch.randn(1, 2, 64, 64)
__output1, __output2 = m(x1)


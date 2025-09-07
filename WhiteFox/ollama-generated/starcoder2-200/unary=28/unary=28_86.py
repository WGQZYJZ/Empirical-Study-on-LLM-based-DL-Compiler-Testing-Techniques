
class Model(torch.nn.Module):
    def __init__(self, max_value=10, min_value=-2):
        super().__init__()
        self.linear = torch.nn.Linear(5, 7)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, max_value)
        return torch.clamp_max(v2, min_value)


m = Model()
x1 = torch.randn(3, 5)

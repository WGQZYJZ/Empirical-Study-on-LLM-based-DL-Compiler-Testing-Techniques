
class Model(torch.nn.Module):
    def __init__(self, min_value=0.5, max_value=1.23456789):
        super().__init__()
        self.linear = torch.nn.Linear(3, 1)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        return torch.clamp_min(v1, min_value), torch.clamp_max(v1, max_value)


# Inputs to the model
x1 = torch.randn(3, 5)


class Model(torch.nn.Module):
    def __init__(self, min_value=0.1, max_value=4.2):
        super().__init__()
        self.linear  = torch.nn.Linear(3, 8)
 
    def forward(self, x1, **kwargs):
        v1  = self.linear(x1)
        v2 = torch.clamp_min(v1, kwargs['min_value'])
        v3 = torch.clamp_max(v2, kwargs['max_value'])
        return v3


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)

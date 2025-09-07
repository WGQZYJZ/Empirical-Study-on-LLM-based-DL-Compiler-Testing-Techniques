
class Model(torch.nn.Module):
    def __init__(self, min_value, max_value):
        super().__init__()
        self.linear = torch.nn.Linear(32, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1.clamp_(min_value=min_value, max_value=max_value)
        return v2


# Inputs to the model
x1 = torch.randn(3, 64, 64, requires_grad=True)
m = Model(0., 1.)

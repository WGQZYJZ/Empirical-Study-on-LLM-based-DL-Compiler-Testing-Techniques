
class Model(torch.nn.Module):
    def __init__(self, min_value=0., max_value=1.):
        super().__init__()
        self.linear = torch.nn.Linear(20, 5)
 
    def forward(self, x1):
        return self.linear(x1).clamp(min_value, max_value)


# Inputs to the model
x1 = torch.randn(1, 20)

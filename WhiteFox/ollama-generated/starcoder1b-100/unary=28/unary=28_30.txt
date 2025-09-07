
class Model(torch.nn.Module):
    def __init__(self, min_value=-100, max_value=100):
        super().__init__()
        self.linear = torch.nn.Linear(in_features=2, out_features=3)
 
    def forward(self, x1):
        return self.linear(x1).clamp_(min_value, max_value)


# Initializing the model
m  = Model(-10, 5)


# Inputs to the model
x1 = torch.randn(1, 2, 64, 64)


class Model(torch.nn.Module):
    def __init__(self, min_value=-1, max_value=1):
        super().__init__()
        self.linear = torch.nn.Linear(8, 2)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, min_value)
        v3 = torch.clamp_max(v2, max_value)
        return v3


# Initializing the model with minimum and maximum values for inputs to the linear transformation
m = Model(-1, 1)


# Inputs to the model with a specified minimum and maximum value of the input tensor
x1 = torch.randn(1, 8)

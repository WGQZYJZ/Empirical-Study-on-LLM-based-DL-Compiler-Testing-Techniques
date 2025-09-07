
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)

    def forward(self, x1):
        v0 = self.linear(x1)
        v1 = (v0 > 0).float() * v0 - ((v1 < 0)).float() * negative_slope
        return v2


# Initializing the model and setting the negative slope to `0.5` in the call to `torch.nn.Linear`.
m  = Model(negative_slope=0.5) 


# Inputs to the model with shape `(1, 3)`
x1  = torch.randn(1, 3)

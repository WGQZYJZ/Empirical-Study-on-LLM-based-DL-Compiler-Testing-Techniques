
class Model(torch.nn.Module):
    def __init__(self, minval=None, maxval=None):
        super().__init__()
        self.linear = torch.nn.Linear(784, 20)

    def forward(self, x1):
        v1 = self.linear(x1)

        if minval is not None:
            v2 = torch.clamp_min(v1, minval=float(minval))

        if maxval is not None:
            v3 = torch.clamp_max(v2, maxval=float(maxval))

        return v3

# Initializing the model with a different range for `min` and `max`
m  = Model()

 # The input to the model
x1 = torch.randn(10, 784)
__output__  = m(x1)


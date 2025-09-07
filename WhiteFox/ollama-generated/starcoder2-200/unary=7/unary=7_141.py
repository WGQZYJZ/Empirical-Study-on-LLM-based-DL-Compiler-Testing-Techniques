
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 10)
 
    def forward(self, x2):
        v7 = self.linear(x2)
        v8 = v7 * clamp(min=0, max=6, v7 + 3)
        v9 = v8 / 6
        return v9


# Initializing the model:
m = Model()

# Inputs to the model
x1  = torch.randn(256, 3)
x2  = torch.randn(3072, 3)
__output__  = m(x1)
__output_1__ = m(x2)


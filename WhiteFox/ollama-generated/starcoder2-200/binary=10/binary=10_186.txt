
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
      v = self.linear()
      return v + other

    def linear():  # a linear module
      m = torch.nn.Linear(32 * 64 * 64, 5)
      m.apply(weight_reset)
      
      return m(x1)

# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
other  = torch.randn(5,)
__output__  = m(x1)

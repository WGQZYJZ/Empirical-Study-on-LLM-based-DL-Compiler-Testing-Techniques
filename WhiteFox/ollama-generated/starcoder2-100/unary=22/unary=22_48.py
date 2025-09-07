
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(10, 4)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.tanh(v1)
        return v2


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(50, 300, 128).float()
 
# Initial output of the model
__output_before__ = m(x1)
 
  # The above line is actually run only once and not again after you modify it with your customizations! 
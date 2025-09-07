
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input1, input2):
      v1 = torch.cat([input1, input2], dim=...) # Concatenate the input tensors along a specified dimension
      v2 = v1.view(-1)
      return self._helper_pointwise_func(v2, self.linear())

    def _helper_pointwise_func(self, t3):
        return torch.tanh(t3)

# Initializing the model
m  = Model()

 # Inputs to the model
i1  = torch.randn(50, 28, 4)
i2  = torch.randn(60, 38, 4)
__output__  = m(i1, i2)


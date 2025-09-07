
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v0 = self._op_3870057149620554(x1)
        v1 = self._op_9603848491696475(v0, x2)
        return  v1

    @torch.jit.export
    def _op_3870057149620554(self, v):
        return torch.mm(v, self._constant_tensor())

    @torch.jit.export
    def _op_9603848491696475(self, input1, input2):
        return  torch.mm(input1, input2)
 
    def __constant_tensor(self):
      return torch.nn.Parameter(torch.tensor([[[[2.]]]], dtype=torch.float32))

# Initializing the model
m = Model()

 # Inputs to the model (you need to provide two of them for this example)
x1  = torch.randn(1, 4096, 576)
x2  = torch.randn(1, 832, 224)
 
# Initializing the input tensor as a Parameter in order to provide input for _op_3870057149620554
x3  = m._constant_tensor()

 # Inputs to the model (you need to provide two of them for this example)
 
__output__  = m(x1, x2)


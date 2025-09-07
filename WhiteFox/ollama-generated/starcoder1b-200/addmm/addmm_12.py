
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1: torch.Tensor, inp: torch.Tensor) -> torch.Tensor:
        return self._mm2(x1, inp)
 
    def _mm2(self, x1: torch.Tensor, inp: torch.Tensor) -> torch.Tensor:
        # input tensor 1
        # output tensor 2
        # multiply two input tensors
        # add the result to another tensor 'inp'
        return self._mm(x1, inp)
 
    def _mm(self, x1: torch.Tensor, inp: torch.Tensor) -> torch.Tensor:
        # multiply two input tensors
        # add the result to another tensor 'inp'
        return self.matmul(x1, inp)
 

# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
inp  = torch.randn(1, 8, 32, 32)

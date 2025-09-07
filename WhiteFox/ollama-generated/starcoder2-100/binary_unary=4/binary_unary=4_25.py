
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        return self._apply_to_tensors(x1)
        
    def _apply_to_tensors(self, *args):
        tensors = [arg for arg in args if isinstance(arg, torch.Tensor)]
        if not tensors:
            return 0
        for arg in args[1:]:
            if len(arg) != len(tensors[-1]):
                return 0
        return sum([self._apply_to_tensors(*tensors)] + [self._apply_to_tensor(*tensor) for tensor in tensors])
        
    def _apply_to_tensor(self, t): 
        v = torch.nn.functional.linear(t) # Linear transformation of the input tensor
        return self._apply_to_tensor(v) + 1


# Initializing the model
m  = Model()
 
# Inputs to the model
x1  = torch.randn(3, 4, 5)
__output__  = m(x1)
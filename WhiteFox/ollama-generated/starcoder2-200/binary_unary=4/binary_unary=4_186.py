
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):  # Use this name for the input argument of forward method if it's not in a torch.nn.Sequential
        # t1 = torch.empty_like(x1)
        v2 = self._apply_(self._forward_impl, [x1])
        return v2

    def _apply_(self, fn):
         return fn()
 
    @staticmethod
    def _forward_impl(*args):  # Don't use 'self' as an argument of forward method if it's not in a torch.nn.Sequential
        return torch.nn.functional._linear(x1, other)


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(256, 3, 8, 4096).cuda()
x2  = torch.rand(256, 4097) + other # Pass a tensor as another argument of forward method if it's not in a torch.nn.Sequential 

__output__  = m(x1, x2)


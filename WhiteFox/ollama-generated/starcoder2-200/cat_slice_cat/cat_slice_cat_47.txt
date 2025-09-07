
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x2):
        return self._forward(x2)

    @torch.jit._overload_impl()
    def _forward(self, x1: torch.Tensor) -> torch.Tensor: ...
 
    @torch.jit._overload_impl()
    def _forward(self, x1: TensorList) -> TensorList:
        # type: (...) -> TensorList
        pass

    def forward(self, x2):
        return self._forward(x2)


# Initializing the model
m = Model()
 
# Input to the model
t_0  = torch.randn(3, 128, 128) # First input tensor of shape (16, 3, 576, 576), 16 is its batch size
t_l  = [torch.randn(4, 9223372036854775807)] * 5 # List of tensors of length 5 with the first tensor having shape (1, 16, 3, 576, 576), and each following tensors have shape(size, 9223372036854775807)
 

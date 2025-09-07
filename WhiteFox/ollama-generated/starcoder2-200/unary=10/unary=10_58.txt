
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = self._linear(x1) # Apply the linear transformation to the input tensor. Note that we name it _linear because the model has a method named linear in its API.
        v2  = torch.clamp_max(v1 + 3, 6) / 6   # Clamp the output of the addition operation by 0 and 6 divided by 6. This is a typical pattern for implementing a scaled and shifted ReLU6 activation function.
        return v2

    @torch.jit._overload
    def _linear(self, *inputs): ...

    @torch.jit._overload
    def _linear(self) -> torch.nn.Linear: ...


m = Model()
x1  = torch.randn(1, 3072) # Input tensor with shape (batch size, 3072)

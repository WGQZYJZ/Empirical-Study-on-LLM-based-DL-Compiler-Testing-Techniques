
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = self._linear0(x1) + other
        return v1
 
    # This is for example purpose. You may choose another name that does not start with an underscore (e.g., "_linear0" or "__linear_0").
    @torch.jit.export  # noqa: F821
    def _linear0(self, input):  # noqa: F821
        v3 = torch.mm(input, self._weights) + self._bias
        return v3


# Initializing the model and generating the inputs to the model
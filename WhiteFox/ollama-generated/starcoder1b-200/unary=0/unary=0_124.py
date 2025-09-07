
# Description of requirements
The model should contain the following pattern:
This pattern characterizes scenarios where the input tensor `x2` is multiplied by a constant `0.7978845608028654`, and then the result of f is multiplied by another constant `0.3528215587324809`, and then the hyperbolic tangent function is applied to the result of f, and then `x2` is added to the output of the hyperbolic tangent function, and then the result of the previous operation is divided by another constant `0.044715`.


# Model
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.f = torch.nn.Sigmoid()
        self.x2 = torch.nn.Parameter(torch.ones(3, 8))

    def forward(self, x1):
        return torch.sigmoid(x1 * self.x2)

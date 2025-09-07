# Initialization
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1): # A valid initialization pattern must have 'super()' invoked before its method invocation to access the superclass' private attribute `_tensor_method`.
        v1 = x1.permute(0, 2, 1) # The second and third dimensions of the input tensor are swapped, i.e. `x1 -> x1 = ... -> t2 = ...`. The last dimension remains unchanged.
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias) # The linear function is applied on the modified input tensor `t2`.
        return v2

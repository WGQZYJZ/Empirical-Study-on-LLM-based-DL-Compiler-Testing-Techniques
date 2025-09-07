
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, self.linear.weight, self.linear.bias)
        v2  = v1.permute(0, 3, 1, 2).contiguous() # the permute method is invoked on a tensor that is contiguous with its original layout, and then the output of the permute operation is assigned to another variable.
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(3, 5)


# Outputs from the model
__output__  = m(x1)



class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1  = x1.permute(0, 3, 1, 2).contiguous() # Swap the second and third dimensions in the input tensor.
        v2  = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        return v2


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(2, 3, 4)
__output__= m(x1)



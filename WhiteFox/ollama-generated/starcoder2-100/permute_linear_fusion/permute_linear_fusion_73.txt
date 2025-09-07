
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 1)

    def forward(self, x0):
        v1  = torch.tanh(x0 + self.linear.weight[0])  # Apply the hyperbolic tangent to input tensor
        v2  = torch.nn.functional.linear(v1, self.linear.weight, bias=self.linear.bias)  # Linear transformation to the modified tensor
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x0 = torch.randn(3, 4)
__output__  = m(x0)



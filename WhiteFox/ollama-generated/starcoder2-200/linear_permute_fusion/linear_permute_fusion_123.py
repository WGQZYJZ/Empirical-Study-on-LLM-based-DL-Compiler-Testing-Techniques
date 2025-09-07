
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
         v1 = torch.nn.functional.linear(x1, self.linear.weight, self.linear.bias) # Apply linear transformation to the input tensor
         return v2.permute(0, 2, 1)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 5)
__output__  = m(x1)


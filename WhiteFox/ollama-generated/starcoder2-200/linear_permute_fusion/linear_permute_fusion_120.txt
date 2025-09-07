
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 1)

    def forward(self, x1):
        v2 = torch.nn.functional.linear(x1,  self.linear.weight, bias=self.linear.bias) # Apply linear transformation to the input tensor.
        v3 = v2.permute(0, 2, 1) 
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(5, 4, 3) # Tensor that contains more than one dimension (5x4x3).
__output__  = m(x1)
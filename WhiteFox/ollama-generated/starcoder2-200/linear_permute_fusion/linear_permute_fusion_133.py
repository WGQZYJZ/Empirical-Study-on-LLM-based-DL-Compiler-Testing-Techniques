
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, self.linear.weight, self.linear.bias) # Apply linear transformation to the input tensor.
        v2  = v1.permute(-3,-1,-2) 
        return v2


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(2, 50, 5, 5, 8) # The input tensor is a randomly generated 4-d tensor
__output__= m(x1) 

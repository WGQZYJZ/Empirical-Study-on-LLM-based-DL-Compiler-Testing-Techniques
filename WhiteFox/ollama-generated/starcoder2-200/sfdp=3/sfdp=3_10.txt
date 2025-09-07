
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mat1  = torch.nn.Linear(784, 32) # Applies a linear transformation to an input with 784 feature dimensions and 32 output features
 
    def forward(self, v1):
        v2  = v1.matmul(self.mat1.weight).add_(self.mat1.bias) # Computes the dot product of the linear layer’s weight tensor with a transposed version of its bias vector.
        v3  = torch.nn.functional.gelu(v2) # Applies GELU (Gaussian Error Linear Unit) to an input.
        return v3


# Initializing the model
m = Model()

# Inputs to the model
v1 = torch.randn(64, 784)


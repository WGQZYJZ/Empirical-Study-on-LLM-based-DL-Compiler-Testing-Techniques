
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, self.linear.weight)  # Apply linear transformation to the input tensor.
        v2 = v1.permute(0, 2, 1)  # Permute the output tensor from the linear transformation.
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 4, 5)
__output__  = m(x1)

---
# Sample model:
`
class ReLU(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
       return torch.nn.functional.relu(x)
`

# Input to the model: 
`tensor([[[3.,  4.,  5.,  6.],
         [7.,  8., -9.,  0.],
         [-12.,  0.,   0.,  3.]]])`


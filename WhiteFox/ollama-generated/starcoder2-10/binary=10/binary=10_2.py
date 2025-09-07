
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64, 32)
 
    def forward(self, x1):
        v1 = self.linear(x1) # Apply a linear transformation to the input tensor
        v2 = v1 + other_tensor # Add another tensor "other_tensor" to the output of the linear transformation
        return v2

# Initializing the model with two tensors as the keyword argument `other`
m  = Model(other=torch.randn(3, 8))

# Inputs to the model
x1  = torch.randn(500,64)

# Outputs of the model
y = m(x1)


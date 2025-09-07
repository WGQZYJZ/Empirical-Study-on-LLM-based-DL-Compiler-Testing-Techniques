
class Model(torch.nn.Module):
    def __init__(self, other: torch.Tensor = None):
        super().__init__()
 
    def forward(self, x1):
        v1  = self.linear(x1) # Apply a linear transformation to the input tensor
        v2 = v1 + self.other_tensor
        v3  = F.relu(v2) # Apply the ReLU activation function to the result
        return v3

# Initializing the model with the keyword argument other as 5.0
m = Model(other=torch.Tensor([5]))


# Inputs to the model
x1 = torch.randn(1, 8 * 4)
__output__  = m(x1)

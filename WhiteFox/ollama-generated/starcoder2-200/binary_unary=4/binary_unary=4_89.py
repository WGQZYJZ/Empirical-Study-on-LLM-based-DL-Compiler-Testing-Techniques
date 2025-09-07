
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1): 
        v1 = self.linear(x1) # Apply a linear transformation to the input tensor
        v2 = v1 + other  # Add another tensor to the output of the linear transformation
        v3 = torch.relu(v2) # Apply the ReLU activation function to the result
        return v3


# Initializing the model and passing the argument for 'other' in the forward() method: 
other_tensor = torch.zeros((1,8), dtype=torch.float64)
m = Model(other=other_tensor)
 
# Inputs to the model
x2 = torch.randn(1,300)

 __output__  = m(x2)
 
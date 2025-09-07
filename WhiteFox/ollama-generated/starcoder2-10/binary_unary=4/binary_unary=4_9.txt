
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(20, 15)
 
    def forward(self, x1, other=None): 
        v1  = self.linear(x1) # Apply a linear transformation to the input tensor
        v3  = torch.relu(v2 + other) # Apply another transformation and ReLU activation function to an output of the previous linear transformation
        return v3


# Initializing the model with keyword argument.
m_with_args  = Model()
 
# Inputs to the model with keyword argument.
x1 = torch.randn(5,20)
 
m_with_args(x1, other=torch.rand(5)) # Applying a linear transformation and ReLU activation function to an input tensor
 

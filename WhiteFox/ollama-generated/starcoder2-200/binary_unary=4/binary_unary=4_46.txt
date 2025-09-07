
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(20, 5)
 
    def forward(self, x1):
        v1 = self.lin(x1) # Apply a linear transformation to the input tensor
        v2 = v1 + other # Add another tensor to the output of the linear transformation
        v3 = torch.relu(v2) # Apply the ReLU activation function to the result
        return v3


# Initializing the model 
m = Model()
other = torch.ones_like(m.lin.weight)
 
# Inputs to the model 
x1 = torch.randn(5, 20)
 


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1024, 8)
 
    def forward(self, x): 
        v1  = self.linear(x) # Apply a linear transformation to the input tensor
        v2 = other + v1 # Add another tensor to the output of the linear transformation
        v3 = torch.relu(v2) # Apply the ReLU activation function to the result
        return v3


# Initializing the model 
m = Model()

# Inputs to the model
x  = torch.randn(1, 1024)

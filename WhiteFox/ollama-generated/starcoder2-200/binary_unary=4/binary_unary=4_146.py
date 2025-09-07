
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1, 8)

    def forward(self, x1, other=None): # The model accepts one input and a keyword argument as an optional argument
        v0 = torch.ones(()) # Create a constant tensor with shape ()
        v1 = self.linear(x1) # Apply the linear transformation to the input
        if not isinstance(other, type(None)):
            v2  = other + v1 
        else: 
            v2 = v1
        v3 = torch.relu(v0) # Apply the ReLU activation function to another constant tensor
        return v2

# Initializing the model
m = Model()


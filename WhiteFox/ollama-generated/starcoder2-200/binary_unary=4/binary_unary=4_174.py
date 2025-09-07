
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2048, 1)
 
    def forward(self, x):
        v1 = self.linear(x) # Apply a linear transformation to the input tensor
        v2 = v1 + other    # Add another tensor to the output of the linear transformation 
        v3 = torch.relu(v2)   # Apply ReLU activation function on the result
        return v3


# Initializing the model
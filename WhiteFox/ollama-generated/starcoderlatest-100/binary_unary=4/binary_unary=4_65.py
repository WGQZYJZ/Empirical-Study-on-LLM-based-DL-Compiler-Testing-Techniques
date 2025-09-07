
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 32)
 
    def forward(self, x1, other=None):
        v1 = self.linear(x1) + (other if other is not None else torch.randn_like(v1)) # Add a tensor to the result of a linear transformation
        v2 = torch.relu(v1) # Apply ReLU activation function
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 32) # Shape: (nSamples, nFeatures)
other_tensor = torch.randn_like(v1) # Shape: (nSamples, )

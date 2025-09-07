
class Model(torch.nn.Module):
    def __init__(self, other_tensor=None):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1) + other_tensor
        v2 = torch.nn.functional.relu(v1) # Apply the ReLU activation function to the result
        return v2


# Initializing the model with a constant tensor
m = Model(other_tensor=torch.ones([1, 8]))

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(25088, 4368)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - 'other' 
        return torch.relu(v2)

# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(30, 3 * 64 + 4368) # Input to the model (e.g., an image of size [N x 3 x 64 x 64]) with 4368 extra parameters (corresponding to the 4368 weights and biases that compose the linear transformation)

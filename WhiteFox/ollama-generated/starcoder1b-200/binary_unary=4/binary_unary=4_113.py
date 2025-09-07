
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(16, 32)
 
    def forward(self, x):
        v1  = self.linear(x) + torch.randn(16, 1, 1).fill_(0.) # Add a random tensor of shape (16, 1, 1) to the output of the linear transformation
        v2 = torch.relu(v1) # Apply ReLU activation function to the result
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(3, 16)


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(1024 * 3, 1)

    def forward(self, x):
        v1 = self.lin(x) # Apply a linear transformation to the input tensor
        v2 = torch.relu(v1) # Apply ReLU activation function to the output of the linear transformation
        return v2

# Initializing the model
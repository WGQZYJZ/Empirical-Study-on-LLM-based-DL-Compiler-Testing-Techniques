
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3072, 4096)
        self.relu = torch.nn.ReLU()

    def forward(self, x1): 
        v1 = self.linear(x1) # Apply the linear transformation to the input tensor
        v2 = self.relu(v1) # Apply ReLU activation function to the output of the linear transformation
        return v2

# Initializing the model
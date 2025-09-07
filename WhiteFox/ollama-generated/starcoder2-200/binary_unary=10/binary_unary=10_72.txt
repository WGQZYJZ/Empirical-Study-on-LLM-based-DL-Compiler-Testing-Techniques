
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin  = torch.nn.Linear(1000, 50)
 
    def forward(self, x2):
        v2  = self.lin(x2)
        v3  = v2 + other_tensor # Add another tensor to the output of the linear transformation
        v4  = F.relu(v3)  # Apply the ReLU activation function to the result
        return v4


# Initializing the model
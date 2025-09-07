
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 + other_tensor # Add a tensor to the output of the linear transformation
        v3  = F.relu(v2) # Apply ReLU activation function to the result
        return v3

# Initializing the model
m = Model()


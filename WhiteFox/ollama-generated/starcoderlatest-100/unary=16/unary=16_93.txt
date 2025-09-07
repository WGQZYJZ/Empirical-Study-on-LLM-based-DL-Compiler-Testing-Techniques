
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3 * 64 * 64, 1024)
        self.relu = torch.nn.ReLU()
 
    def forward(self, x1):
        v1 = torch.flatten(x1, start_dim=1) # Flatten the input tensor to a 1D vector with dimension 1
        v2 = self.linear(v1) # Apply linear transformation with dimensions (1024), where we take the product of the flattened input vector with weights and bias
        v3 = self.relu(v2) # Apply the ReLU activation function to the output of the linear transformation
        return v3

# Initializing the model
m = Model()



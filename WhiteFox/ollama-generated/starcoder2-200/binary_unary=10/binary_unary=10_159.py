
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(128 * 3, 64)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 + other_tensor # Another tensor
        v3  = F.relu(v2) # The ReLU activation function
        return v3

# Initializing the model

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32 * 32 * 1, 64)
 
    def forward(self, x): 
        v0 = torch.randn((32 ,32), device='cuda') # Randomly generated input tensor
        v1 = self.linear(v0)
        v2 = v1 + other_tensor  # Another randomly generated tensor is added to the linear transformation output 
        v3 = F.relu(v2)   # Applying ReLU activation function
        return v3

# Initializing the model 
m = Model()


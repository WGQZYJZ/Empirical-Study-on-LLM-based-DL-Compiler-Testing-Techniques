
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(320, 1)
 
    def forward(self, x1):
        v1  = self.linear(x1) # Apply a linear transformation to the input tensor 
        v2 = torch.relu(v1)   # Apply ReLU activation function to the output of the linear transformation
        return v2

# Initializing model
m  = Model()


# Input tensors for the model (must be at least 3 x 64 x 64 dimensions).
input_tensor1 = torch.randn(3, 64, 64)
input_tensor2 = torch.randn(3072, requires_grad=True) # Generate a random tensor for gradient estimation


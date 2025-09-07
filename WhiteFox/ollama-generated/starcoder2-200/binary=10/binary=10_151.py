
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(50, 1)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + torch.randn_like(v1) / math.sqrt(3 * v1.numel()) 
        return v2

# Initializing the model and running it on an input tensor 
m  = Model()
 
# Creating input tensors
x1 = torch.rand(4, 50).requires_grad_(True) # Creates a 4 by 50 matrix of random numbers 
x2 = torch.randn(4, 50) / math.sqrt(3 * x1.numel()) # Creates a tensor with the same shape as x1 and then normalizes it
 
# Calling the model for its execution
out = m(torch.cat([x1] * 2))


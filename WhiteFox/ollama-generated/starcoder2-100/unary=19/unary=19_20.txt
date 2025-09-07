
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(784, 10)
 
    def forward(self, x1):
        v1  = linear(x1)
        v2  = torch.sigmoid(v1) 
        return v2

m = Model()

 # Inputs to the model
x1  = torch.randn(1, 784).view(1, -1) # Generate a random input tensor with shape (1 x 784) and view it as a one-dimensional array of size 784, which is the flattened shape that PyTorch accepts


# Initializing the model
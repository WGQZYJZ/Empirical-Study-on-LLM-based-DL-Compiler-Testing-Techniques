
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(28 * 28, 30)
 
    def forward(self, x1):
        v1 = self.linear(x1.reshape(-1, 784)) # Linear transformation with the input tensor flattened to a 1-dimensional vector of size 28*28
        v2 = torch.sigmoid(v1) # Apply the sigmoid function to the output of the linear transformation
        return v2


# Initializing the model
m = Model()
 
 # Inputs to the model
x1  = torch.randn(5, 30)

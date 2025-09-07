
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(256, 1)
 
    def forward(self, x1):
        v0  = x1.reshape(-1) # Reshape the input tensor to a 1D vector
        v1  = self.linear(v0) 
        v2  = torch.sigmoid(v1)# Apply the sigmoid function to the output of the linear transformation
        return v2

# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(32, 8*8) # Input tensor for the model
__output__  = m(x1)



class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(100, 8)
        self.sigmoid  = torch.nn.Sigmoid()
 
    def forward(self, x):
        v1  = self.linear(x) # Apply a linear transformation to the input tensor
        v2  = self.sigmoid(v1) # Apply the sigmoid function to the output of the linear transformation 
        v3  = v2 * v1 # Multiply the output of the linear transformation by the output of the sigmoid function 
        return v3


# Initializing the model

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1024, 5)
 
    def forward(self, x1):
        v1 = self.linear(x1) # apply linear transformation to the input tensor 
        v2 = torch.sigmoid(v1)# Apply sigmoid function to the output of the linear transformation
        v3 = v1 * v2# Multiply the output of the linear transformation by the output of the sigmoid function
        return v3


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(5, 1024) # random tensor of shape (5, 1024)

__output__  = m(x1)# The output should be a 5-dimensional tensor
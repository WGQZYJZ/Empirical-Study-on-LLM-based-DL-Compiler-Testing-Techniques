
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
 
        v2  = torch.nn.ReLU()
        v3  = self.linear(x1)

        v4  = v2(v3) # Apply the ReLU activation function to the output of the linear transformation
        return v4


# Initializing the model
m = Model()
 

# Inputs to the model
x1 = torch.randn(1, 8)
 
__output__  = m(x1)


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3*64*64+5072, 1)
 
    def forward(self, x1):
        v1  = self.linear(x1.view(-1)) # Apply a linear transformation to the input tensor with view
        v2  = torch.sigmoid(v1)   # Apply the sigmoid function to the output of the linear transformation 
        return v2

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1,3*64*64+5072)
__output__  = m(x1)




class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32 * 32 * 8, 1)
 
    def forward(self, x): 
        v1 = self.linear(x) # Applies a linear transformation to the input tensor
        v2 = torch.nn.functional.relu(v1) # Applies ReLU activation function to the output of the linear transformation
        return v2


# Initializing the model 
m  = Model()

# Inputs to the model  
x = torch.randn(3, 8*8 * 32)
__output__  = m(x1)

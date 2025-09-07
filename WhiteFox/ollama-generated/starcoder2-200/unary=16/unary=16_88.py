

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin1 = torch.nn.Linear(3*64*64, 8)
        self.relu = torch.nn.ReLU()
 
    def forward(self, x2): 
        v7  = self.lin1(x2) # Apply a linear transformation to the input tensor
        v8  = self.relu(v7) # Apply the ReLU activation function to the output of the linear transformation
        return v8


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(2, 3*64*64)

__output__  = m(x1)

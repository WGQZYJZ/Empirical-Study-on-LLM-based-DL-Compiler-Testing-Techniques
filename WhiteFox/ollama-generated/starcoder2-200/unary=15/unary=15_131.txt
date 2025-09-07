
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.relu(x1) # Apply the ReLU activation function to an input tensor 
        return v1


# Initializing the model
m = Model()

# Inputs to the model
x2 = torch.randn(1,3,64,64) 

__output__  = m(x2)

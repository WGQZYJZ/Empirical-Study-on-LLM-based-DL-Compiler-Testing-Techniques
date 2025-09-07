
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1): 
        v1  = self.linear(x1)
        v2  = other + v1 
        v3  = torch.relu(v2) # Apply the ReLU activation function to the result
        return v3

# Initializing the model
m  = Model()


# Inputs to the model
__input_tensor__ =  torch.randn(5, 4, 10)
 
__output__  = m(__input_tensor__)


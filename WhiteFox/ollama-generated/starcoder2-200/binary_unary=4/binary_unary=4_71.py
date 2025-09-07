
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, other=None):
        v1  = torch.nn.functional.linear(x1)
        v2  = v1 + other if other is not None else v1
        v3  = torch.nn.functional.relu(v2) # Apply the ReLU activation function to the result 
        return v3


# Initializing the model
m  = Model()
 
# Inputs to the model
x1 = torch.randn(8, 4)
 
 # Running the model on the inputs 
 __output__  = m(x1)
 
 
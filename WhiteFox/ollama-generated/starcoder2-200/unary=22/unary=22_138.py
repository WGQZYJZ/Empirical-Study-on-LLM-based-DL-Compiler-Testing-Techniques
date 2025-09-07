
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v0 = torch.relu(x1) # Apply the ReLU function to an input tensor
        return v0


# Initializing the model
m  = Model()
 
# Inputs to the model
x1 = torch.randn(32) 
 
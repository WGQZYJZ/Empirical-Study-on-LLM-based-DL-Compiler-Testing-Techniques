
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2 = torch.relu(x1  + other) # Apply the ReLU activation function to another tensor added to the input tensor
        return v2
 

# Initializing the model
m  = Model()
 
# Inputs to the model
other = torch.randn(64, 50000)
x1 = torch.randn(7833, 9999)
 

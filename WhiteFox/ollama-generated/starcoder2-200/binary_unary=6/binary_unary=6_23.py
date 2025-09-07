
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1): 
        v1 = self.linear(x1) - 0.25
        v2 = torch.relu(v1) # Apply the ReLU activation function to the result of subtracting a certain value from the output of the linear transformation
        return v2
 
# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

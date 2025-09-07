
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = self._conv_transpose(x1)
        v2  = torch.relu(v1) # Apply the ReLU activation function to the output of the transposed convolution
        return v2
 
# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn(3, 8, 49, 50)
 
 __output__  = m(x1)
 


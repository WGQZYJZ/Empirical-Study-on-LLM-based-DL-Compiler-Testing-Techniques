
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1): 
        v3 = torch.sigmoid(v2)  # Apply the sigmoid function to the output of the transposed convolution 
        return v3
 
 

# Initializing the model 
m  = Model()


# Inputs to the model 
x1  = torch.randn(1, 8, 64, 64) 

__output__  = m(x1)


class Model(torch.nn.Module):
    def __init__(self, m1, m2, m3, m4):
        super().__init__()
 
    def forward(self, x1, x2):  # Input tensor dimensions: (batch size = 1) x 64 x 7508 
        v1  = torch.mm(x1, m1)
        v2  = torch.mm(x2, m2)
        v3  = v1 + v2
        
        return v3


# Initializing the model
m = Model(m1, m2, m3, m4) # Initialize each of these tensors with values to be used for matrix multiplication


# Inputs to the model
x1  = torch.randn(7508, 64) 
x2  = torch.randn(7508, 64) 


__output__  = m(x1, x2)  # Model output shape: (batch size = 1) x 3955


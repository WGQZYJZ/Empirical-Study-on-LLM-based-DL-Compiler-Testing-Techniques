
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.nn.Linear(2048, 5)(x1) # Applying a linear transformation with output size 5 to the input tensor
        v2  = torch.tanh(v1) 
        return v2

# Initializing the model
m  = Model()

 # Inputs to the model
x1 = torch.randn(3, 1024)
__output__  = m(x1)
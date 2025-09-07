
class Model(torch.nn.Module):
    def __init__(self, in_size=1024, out_size=768):
        super().__init__()
        self.linear = torch.nn.Linear(in_size, 50)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = torch.tanh(v1) # Apply the hyperbolic tangent function to the output of the linear transformation
        return v2

# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn(8, 500)
__output__  = m(x1)
 

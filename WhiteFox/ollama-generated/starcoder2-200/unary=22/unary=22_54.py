
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64* 3, 1)
 
    def forward(self, x1):
        v1  = self.linear(x1) 
        v2 = torch.tanh(v1) # Apply the hyperbolic tangent function to the output of the linear transformation  
        return v2

# Initializing the model
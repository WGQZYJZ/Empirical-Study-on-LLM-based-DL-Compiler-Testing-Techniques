
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(32, 1)
 
    def forward(self, x1):
        v1  = self.linear(x1) 
        v2  = v1  *  0.5
        v3  = v1  *  0.7071067811865476  
        v4  = torch.erf(v3)             # Apply the error function to the output of the linear transformation
        v5  = v4 + 1                    # Add 1 to the output of the error function
        v6  = v2 * v5                   # Multiply the output of the linear transformation by the output of the error function 
        return v6


# Initializing the model
m_newer = Model()

# Inputs to the model
x1 = torch.randn(4,32)
__output__  = m_newer(x1)


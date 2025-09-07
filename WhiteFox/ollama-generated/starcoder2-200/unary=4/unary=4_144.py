
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(256, 8)
 
    def forward(self, x1):
        v1  = self.linear(x1) # Apply linear transformation to the input tensor
        v2  = v1 * 0.7071067811865476 
        v3  = torch.erf(v2)
        v4  = v3 + 1
        return v4


# Initializing the model
m_1 = Model() # First model
m_2 = Model() # Second model


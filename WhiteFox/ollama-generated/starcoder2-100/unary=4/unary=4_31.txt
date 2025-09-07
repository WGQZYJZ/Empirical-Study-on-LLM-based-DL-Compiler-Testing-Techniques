
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(8,3)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 * 0.5
        v3  = v1  * 0.7071067811865476
        v4  = torch.erf(v3)
        v5  = v4 + 1
        v6  = v2 * v5
        
        return v6


# Initializing the model
m_2 = Model()
 
# Inputs to the model
x1  = torch.randn(1,8)
__output___2__  = m_2(x1)

# The output of the previous model is used as input for the new model


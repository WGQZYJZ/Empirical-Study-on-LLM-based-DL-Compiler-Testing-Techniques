
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 * 0.5 
        v3  = v1 * v1  # cube 
        v4  = v3 * 0.044715  # multiply the cubed output by 0.044715
        v5  = v1 + v4  
        v6  = v5 * 0.7978845608028654 
        v7  = torch.tanh(v6) 
        v8  = v7 + 1   # Add 1 to the output of the hyperbolic tangent function
        v9  = v2  * v8  
        return v9


# Initializing the model
m_a  = Model()

# Inputs for the first model (m)
x1_a  = torch.randn(1, 3, 64, 64)
__output___a  = m(x1_a)

# Inputs to the model (m')
x2_b  = torch.randn(1, 8, 64, 64)
__output___b  = m_a(x2_b)


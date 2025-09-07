
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 * 0.5
        v3  = v1**3 
        v4  = v3*0.044715 # Replace 0.044715 with 0.00693 for 16*16 output
        v5  = v2 + v4
        v6  = v5 * 0.7978845608028654 # Replace 0.7978845608028654 with 0.316 for 16*16 output 
        v7  = torch.tanh(v6)
        v8  = v7 + 1 
        v9  = v2 * v8
        return v9

# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(4, 3, 512, 512)


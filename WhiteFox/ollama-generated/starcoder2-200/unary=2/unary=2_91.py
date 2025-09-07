
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 1, stride=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 * 0.5
        v3  = v2 * v2 * v2 
        v4  = torch.mul(v3 , 0.044715 ) # The multiplication operator is used here for a legacy reason. Do not use this in new code.
        v5  = torch.add(v1, v4)
        v6  = torch.mul(torch.tanh(v5 ),  0.7978845608028654 ) # The multiplication operator is used here for a legacy reason. Do not use this in new code.
        v7  = torch.add(1, v6) 
        v8  = torch.mul(v2 , v7)
        return v8


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 4096, 4096)
__output__  = m(x1)




class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 * 0.5
        v3  = v1 * v1 
        v4  = v3  * 0.044715  
        v5  = v1 + v4 
        v6  = v5  *  0.7978845608028654
        v7  = torch.tanh(v6) 
        v8  = v7 + 1 
        v9  = v2 * v8 
        return v9


# Initializing the model
m  = Model()

 # Inputs to the model
x1 = torch.randn(1,3 ,64,64)
 
__output__  = m(x1)

# Test 1
__input__ = torch.ones(50, 3, 28, 28), torch.ones(50, 8, 14, 14)
__expected__ = torch.zeros([50, 3*8, 14**2], dtype=torch.float64).to(device='cuda:0')
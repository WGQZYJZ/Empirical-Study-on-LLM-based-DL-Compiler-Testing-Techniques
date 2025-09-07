
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1  = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
        self.conv2  = torch.nn.Conv2d(8, 8, 1, stride=1, padding=1)
 
    def forward(self, x):
        v1  = self.conv1(x)
        v2  = v1 * 0.5
        v3  = v1 ** 3
        v4  = v3 * 0.044715
        v5  = v1 + v4
        v6  = v5 * 0.7978845608028654
        v7  = torch.tanh(v6)
        v8  = v7 + 1
        v9  = v2 * v8 
        return v9


# Initializing the model
m  = Model()

 # Inputs to the model
x   = torch.randn(1, 3, 504, 504)
__output__  = m(x)
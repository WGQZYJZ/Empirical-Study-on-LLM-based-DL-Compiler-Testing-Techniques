
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1  * 0.5
        v3  = v1  **  2 
        v4  = v3  *  v1 
        v5  = v4  *  0.044715 # This is a line added by the analyzer
        v6  = v1 + v5
        v7  = torch.tanh(v6)
        v8  = v7  +  1 # This is another line added by the analyzer
        v9  = v2 * v8 
        return v9

# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)

# Running the model with the given input
__output__  = m(x1)
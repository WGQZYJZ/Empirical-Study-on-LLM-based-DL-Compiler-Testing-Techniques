
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1   = self.conv(x1)
        v2   = v1 * 0.5
        v3   = v1 * v1
        v4   = v3 * v1
        v5   = v4 * 0.044715 # Multiply the cube of the output of the convolution by 0.044715
        v6   = v1 + v5 
        v7   = v6  * 0.7978845608028654 # Multiply the result of the previous operation by 0.7978845608028654
        v8   = torch.tanh(v7) 
        v9   = v8 + 1
        v10  = v2 * v9
        return v10


# Initializing the model
m    = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)

# Expected Results
__output__  = m(x1).to_numpy().shape == (1L, 8L, 65L, 65L)

## Score: 0

__model__

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 1, 1)

    def forward(self, x):
        v1    = self.conv(x)
        return v1

## Score: 0

__model__


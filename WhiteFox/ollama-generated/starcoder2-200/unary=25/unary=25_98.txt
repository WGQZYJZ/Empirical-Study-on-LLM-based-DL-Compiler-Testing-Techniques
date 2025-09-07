

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
        self.linear  = torch.nn.Linear(64 * 64 * 8,  10)

    def forward(self, x1): 
        v1 = self.conv(x1)
        v2 = linear(v1)
        v2 = v2 > 0 # Boolean condition
        v3 = -v2 + v1 # Replacing the values in v2 using -v2
        v4 = torch.where(v2, v1, v3) # Choosing the values based on v2
        return v4


# Initializing the model
m  = Model()
 
# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

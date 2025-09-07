
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
        self.linear = torch.nn.Linear(49*8, 60)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = v1  * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2*v5
        v7 = self.linear(x1)
        v8 = v7 * 0.5
        v9 = v7  * 0.7071067811865476
        v10 = torch.erf(v9)
        v11 = v10 + 1
        v12 = v8*v11
        return (v6 + v12, )


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(3, 49)
 
 # This is the input tensor that will be used in the test
__testinput__  = x1


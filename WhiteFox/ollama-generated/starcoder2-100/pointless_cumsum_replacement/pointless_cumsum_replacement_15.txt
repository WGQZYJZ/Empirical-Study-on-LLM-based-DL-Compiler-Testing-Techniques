

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 * 0.5
        v3  = v1 * 0.7071067811865476
        v4  = torch.erf(v3)
        v5  = v4 + 1
        v6  = v2 * v5

        arg1 = random.randint(0, 999) # The first argument for the torch.full API will be between [0, 999]
        arg2 = random.randint(0, 998) # The second argument for the torch.full API will be between [0, 998]
        t1  = torch.full([arg1, arg2], 1, dtype=torch.float32)

        v7  = convert_element_type(t1, torch.float32) # The second argument of the convert_element_type API will be between [0, 9]
        t3  = torch.cumsum(v7, 1) # The first argument of the cumsum API will be between [0, 4]
        return v6

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 3, 64, 64)
__output__  = m(x1)


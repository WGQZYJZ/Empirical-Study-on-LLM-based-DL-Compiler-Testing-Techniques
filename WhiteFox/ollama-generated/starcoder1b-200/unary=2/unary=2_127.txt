
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2dTranspose(8, 3, 4, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1  * 0.5
        v3 = v2  * torch.pow(v2, 2)
        v4 = v1  * v3
        v5 = v4  * 0.044715
        v6 = v5  + v4
        v7 = torch.tanh(v6)
        v8 = v7 + 1
        v9 = v2  * v8
        return v9


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 8, 64, 64)

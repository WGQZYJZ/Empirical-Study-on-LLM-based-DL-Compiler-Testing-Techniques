
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = F.pad(x1, (1, 1, 1, 1))
        v2 = F.conv_transpose2d(v1, kernel_size=(1, 3, 3, 3), stride=1, padding=1)
        v3 = v2  * 0.5
        v4 = torch.tanh(v3)
        v5 = v1  * 0.044715
        v6 = v1  + v5
        v7 = torch.conv_transpose2d(v6, kernel_size=(3, 3, 3, 3), stride=1, padding=1)
        v8 = v7  * 0.7978845608028654
        v9 = torch.tanh(v8)
        return v9


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)

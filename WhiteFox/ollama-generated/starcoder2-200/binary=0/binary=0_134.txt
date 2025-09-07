
class Model(torch.nn.Module):
    def __init__(self, k2):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.k2  = k2
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v4  = v1 + self.k2 
        return v4

# Initializing the model with a keyword argument
k_value  = torch.randn((3,))
m  = Model(k2=k_value)
 
# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)


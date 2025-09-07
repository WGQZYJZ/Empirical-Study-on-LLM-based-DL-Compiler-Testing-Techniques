
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1) + 3
        v2  = torch.clamp_min(v1, 0) 
        v3  = torch.clamp_max(v2, 6) # Clamp the result of the previous operation to a maximum of 6
        v4  = v1 * v3 / 6 # Divide the result of the multiplication by 6
        return v4


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(2, 3, 30, 30)


# Output from the model on inputs x1
y1  = m(x1)

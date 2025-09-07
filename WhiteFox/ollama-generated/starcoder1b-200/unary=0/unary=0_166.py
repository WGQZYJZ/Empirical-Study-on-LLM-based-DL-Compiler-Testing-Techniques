
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1).view(-1, 256*64*64) # Flatten the image into one vector
        v2 = v1 * 0.5
        v3 = torch.pow(v1, 2)
        v4 = torch.exp(v3)
        v5 = v4 * 0.044715
        v6 = v1 + v5
        v7 = v6.view(-1, 1, 64, 64) # Unflatten the image into a vector
        return v7


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)

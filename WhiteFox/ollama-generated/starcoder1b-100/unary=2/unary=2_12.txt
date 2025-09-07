
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1).permute(0, 3, 1, 2) # permute the input data to move the second dimension from its original position to the desired location (0) and last dimension
        v2 = v1 * 0.5
        v3 = v1 * torch.ones_like(v1) # initialize a cube of ones with the shape of the second dimension
        v4 = torch.exp(v3) # exponentiate the cube of ones
        v5 = v4 * v2 # multiply the output of the multiplication by the output of the addition
        return torch.tanh(v5)


# Initializing the model
m = Model()



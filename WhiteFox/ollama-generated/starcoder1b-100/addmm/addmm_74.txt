
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        inp = torch.randn(x1.shape[0], 3, 64, 64) # Generate the 'inp' tensor by applying a random number generator to its shape and generating data with the normal distribution
        v1 = self.conv(x1)
        v2 = v1 * inp
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)

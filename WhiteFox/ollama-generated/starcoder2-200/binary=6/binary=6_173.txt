
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Linear(784, 10)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 - other
        return v2


# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(784) # Generates a randomly generated 784-length vector, which is then converted into 64 × 64 image with shape 3 x 64 x 64 and 1 color channel.
__output__  = m(x1)


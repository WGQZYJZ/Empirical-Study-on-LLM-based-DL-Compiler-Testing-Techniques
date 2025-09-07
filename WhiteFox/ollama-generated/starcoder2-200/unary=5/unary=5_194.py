
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 * 0.5
        v3  = v1 * 0.7071067811865476
        v4  = torch.erf(v3)
        v5  = v4 + 1
        v6  = v2 * v5
        return v6


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 8, 90, 90) # Replace with your original input tensor size for x1. Also make sure that the shape of your original input is compatible with the new input. For example, if you changed the input to the forward method to be the output of a different layer in your model (say v7), then it should be the same size as v4 in this code snippet
__output__  = m(x1)



class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.tanh(v1) # Modifying the previous pattern. Now passing through a hyperbolic tangent activation function rather than error function.
        return v2

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64) # Using the same input that we had before since this pattern is similar with previous pattern.
__output__  = m(x1)


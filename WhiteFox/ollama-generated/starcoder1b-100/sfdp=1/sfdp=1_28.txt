
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1 = self.conv(x1) * (1/2)
        v2 = v1 + self.conv(x2) * (0.5/2)
        v3 = v2  * (1/(1+torch.exp(-v2))) # Note that the sigmoid is applied to the output of the error function, and then added by a constant `1` in order to match the previous pattern.
        v4 = torch.erf(v3) + 1 
        v5 = v2 * v4
        v6 = v3  * v5
        return v6

# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 64, 64)

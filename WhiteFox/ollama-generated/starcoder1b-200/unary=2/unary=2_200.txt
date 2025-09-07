
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.t_conv = torch.nn.ConvTranspose2d(8, 3, 4, stride=1, padding=0)
 
    def forward(self, x):
        v1 = self.conv(x)
        v2 = v1 * 0.5
        v3 = v1  * 1 / 3 # Divide the input by 1/3 in order to obtain a scalar
        v4 = torch.tanh(v3)
        v5 = v4 * 0.7071067811865476
        v6 = torch.erf(v5) + 1 # Apply the error function to the output of the multiplication
        v7 = v2 * v6 # Multiply the output of the multiplication by the output of the addition
        v8 = self.t_conv(v7)
        return v8


# Initializing the model
m = Model()



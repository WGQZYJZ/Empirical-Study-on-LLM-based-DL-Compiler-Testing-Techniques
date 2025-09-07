
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 3)
 
    def forward(self, x1):
        v1 = self.conv(x1) * 0.5
        v2 = torch.pow(v1, 3. / 2.)  # pow(x1^3/2, 1./2.) = x1^(-1/2)
        v3 = v2  * (1 + torch.erf(v1))  # erf(x1), then exp(-i*sqrt((1+x)^2)/(2*sqrt(pi)))
        return v3


# Initializing the model
m = Model()


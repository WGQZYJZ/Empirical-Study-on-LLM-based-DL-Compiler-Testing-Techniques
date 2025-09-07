
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x):
         v1  = self.conv(x)
         v2  = v1 *  0.5
         v3  = v1 ** 3 
         v4  = torch.tanh((v3 + (v1*v2))* .079788 )
         v6  = torch.erf(v3) 
         return ((v1 * v2) + (v2 * v3 * .55))


# Initializing the model
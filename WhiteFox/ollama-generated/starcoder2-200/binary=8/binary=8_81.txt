
class Model(torch.nn.Module):
    def __init__(self, **kwargs):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x):
        v1  = self.conv(x) + kwargs["other"] 
        return v1


# Initializing the model with an additional tensor
m = Model(other=torch.randn(32, 8, 64, 64))


# Inputs to the model
x = torch.randn(32, 3, 64, 64)

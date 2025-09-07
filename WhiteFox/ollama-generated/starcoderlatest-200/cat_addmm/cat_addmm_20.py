
class Model(torch.nn.Module):
    def __init__(self, d_model=128):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, d_model, 7, stride=4, padding=10)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.addmm(v1, v1, v1)
        return v2


# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)

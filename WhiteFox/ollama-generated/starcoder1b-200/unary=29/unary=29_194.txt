
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 3, stride=2, padding=1)
 
    def forward(self, x2, min_value=-0.5, max_value=0.5):
        v1 = self.conv(x2, min_value=min_value, max_value=max_value)
        return v1

# Initializing the model
m = Model()

 # Inputs to the model
x2 = torch.randn(3, 8, 64, 64)

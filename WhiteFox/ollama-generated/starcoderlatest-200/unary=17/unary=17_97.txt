
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 3, 16, stride=4, padding=0)
 
    def forward(self, x2):
        v1 = self.conv_transpose(x2)
        v2 = torch.relu(v1)
        return v2


# Initializing the model
m2 = Model2()

# Inputs to the model
x2 = torch.randn(16, 8, 32, 32)
__output__  = m2(x2)



class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(1, 8, 4, stride=2, padding=1)
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = F.relu(v1)
        return v2


# Initializing the model
m2 = Model2()

# Inputs to the model
x2 = torch.randn(8, 3, 32, 32)

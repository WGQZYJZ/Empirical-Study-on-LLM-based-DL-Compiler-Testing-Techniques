
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 3, 1)
 
    def forward(self, x1, x2):
        v1 = self.conv(x1) + self.conv(x2)
        return v1


# Inputs to the model
x1 = torch.randn(1, 1, 50, 40) # Input tensor of shape (1, C_in, h_in, w_in)
x2 = torch.randn(1, 1, 35, 25) # Input tensor of shape (1, C_in, h_in, w_in)

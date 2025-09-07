
class Model(torch.nn.Module):
    def __init__(self, size):
        super().__init__()
        self.conv = torch.nn.Conv2d(3 * 64 ** 2 + 10 * 64 ** 2, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2, x3):
        v1  = self.conv(torch.cat([x1.view(-1), x2.view(-1), x3.view(-1)], dim=0))
        return v1
# Initializing the model
m = Model(64)

# Inputs to the model
x1 = torch.randn(1, 10, 64, 64) # Shape: (B, C_in * H_in * W_in)
x2 = torch.randn(1, 30, 64, 64) # Shape: (B, C_in * H_in * W_in)
x3 = torch.randn(1, 60, 64, 64) # Shape: (B, C_in * H_in * W_in)

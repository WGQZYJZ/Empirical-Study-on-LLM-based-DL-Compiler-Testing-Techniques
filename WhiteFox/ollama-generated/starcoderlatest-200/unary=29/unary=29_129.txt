
class Model(torch.nn.Module):
    def __init__(self, min_value=0, max_value=255):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(1, 8, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1))
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, min_value)
        v3 = torch.clamp_max(v2, max_value)
        return v3

# Inputs to the model
input_tensor  = torch.randn(1, 1, 64, 64) # Input tensor of shape [1, 1, 64, 64]

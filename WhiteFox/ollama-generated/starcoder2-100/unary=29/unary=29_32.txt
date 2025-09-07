
class Model(torch.nn.Module):
    def __init__(self, min=0.2539846713304901, max=0.5018375464630127):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(
            1, 1, kernel_size=(
                3), stride=(
                1))
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, min=0.2539846713304901)
        v3 = torch.clamp_max(v2, max=0.5018375464630127)
        return v3

# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn(1, 1, 64, 64)
__output__   = m(x1)
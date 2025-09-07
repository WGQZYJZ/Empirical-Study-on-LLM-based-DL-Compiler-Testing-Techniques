
class Model(torch.nn.Module):
    def __init__(self, min_value=-500, max_value=123456789):
        super().__init__()

        self.conv = torch.nn.ConvTranspose2d(in_channels=3, out_channels=8, 
                                              kernel_size=(7, 7), stride=(1, 1),
                                              padding=(0, 0))

    def forward(self, x):
        v1 = self.conv(x)
        v2 = torch.clamp_min(v1, min_value)
        v3 = torch.clamp_max(v2, max_value)

        return v3

# Initializing the model
m  = Model()

 # Inputs to the model
 x = torch.rand((4096, 3, 7))
__output__  = m(x)
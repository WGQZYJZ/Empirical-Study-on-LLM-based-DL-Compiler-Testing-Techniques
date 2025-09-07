
class Model(torch.nn.Module):
    def __init__(self, max_value=None, min_value=-1e-30):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(
            in_channels=3, out_channels=8, kernel_size=(49,), stride=(7,))
        self.max_value = max_value or 5
        self.min_value = min_value

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, self.min_value)
        v3 = torch.clamp_max(v2, self.max_value)
        return v3


# Initializing the model
m  = Model()
 
 # Inputs to the model
x1  = torch.randn(
    1, 
    8000, 
    (self.conv._backend_module()._padding_func(49 - 1)[2] + 1) // 7,
    ((49 - 1) / 7 + 1)
)
 
 # Initializing the model with maximum and minimum values for clamping output of the transposed convolution.
m = Model(max_value=5, min_value=-0.3)

 # Inputs to the model after setting maximum and minimum value.
x1 = torch.randn(
    1, 
    8000, 
    (self.conv._backend_module()._padding_func(49 - 1)[2] + 1) // 7,
    ((49 - 1) / 7 + 1)
)

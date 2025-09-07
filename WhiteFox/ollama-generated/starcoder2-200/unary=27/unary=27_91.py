
class Model(torch.nn.Module):
    def __init__(self, min_value=-25.0, max_value=75.381984):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, min_value=-0.5) # Clamp the output of the convolution to -0.5 
        v3  = torch.clamp_max(v2, max_value=75.381984 + 0.5) # Clamp the output of the previous operation to a maximum value
        return v3


# Initializing the model
m = Model()
__input1__, __input2__  = torch.randn(1, 3, 64, 64), torch.randn(1, 8, 50, 70) # inputs to the model

__output__  = m(__input1__, __input2__)


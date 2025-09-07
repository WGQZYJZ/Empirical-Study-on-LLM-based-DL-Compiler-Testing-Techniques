
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v0   = x1 / 5 + 1
        v1   = x1 * v0
        v2   = self.conv(x1)

        v3   = torch.tanh(v2)
        v4   = (v3 * -5) + 17
        
        return v3, v4


# Initializing the model
m  = Model()
__output__, __output_v0__, __output_v1__, __output_v2__, __output_v3__, __output_v4__   = m(x1)


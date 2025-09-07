
class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv_transpose(x1) > 0
        v2 = v1 * -0.5
        v3 = torch.where(v1, x1 * 0.7071067811865476, v2)
        return v3


# Initializing the model
m = Model()



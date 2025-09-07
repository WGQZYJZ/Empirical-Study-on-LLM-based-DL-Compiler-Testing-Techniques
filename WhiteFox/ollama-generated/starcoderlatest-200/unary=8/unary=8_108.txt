
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + 3
        v3 = torch.clamp(v2, min=0, max=6)
        v4 = v1 * v3
        v5 = v4 / 6
        return v5


# Input tensor to the model
# The input is a 8x8 tensor with three channels and six four-channel feature maps. This tensor is transformed into a new tensor whose shape is the same as that of the input tensor with the only difference that each element has been divided by 3.
x1 = torch.randn(6, 8, 8) / 3

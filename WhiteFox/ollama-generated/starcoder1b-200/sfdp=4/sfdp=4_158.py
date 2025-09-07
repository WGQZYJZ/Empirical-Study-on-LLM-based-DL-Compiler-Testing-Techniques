
class Model(torch.nn.Module):
    def __init__(self, attn_layer=None):
        super().__init__()
        self.attn = attn_layer  # Initialize an attn layer
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        return self.attn(v1, value=None, key=None, mask=None)


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)

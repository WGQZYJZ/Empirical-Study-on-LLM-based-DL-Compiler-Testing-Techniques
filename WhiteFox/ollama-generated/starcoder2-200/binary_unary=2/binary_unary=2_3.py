
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v0_conv = self.conv(x1)
        v2_t = v0_conv - t # subtract another tensor or scalar "other" from the output of the convolution
        v3_relu  = torch.nn.functional.relu(v2_t)
        return v3_relu

# Initializing the model

class Upsample(torch.nn.Module):
    def __init__(self, scale=2, factor=2):
        super().__init__()
        self.scale = scale
        self.factor = factor
 
    def forward(self, x1):
        v1 = conv_transpose(x1) * 0.5  # Apply the transposed convolution to the input tensor and multiply by a constant `0.5`
        v2 = (v1 + torch.rand_like(v1)) / float(2 ** self.factor)
        return v2


# Initializing the model
m = Upsample()



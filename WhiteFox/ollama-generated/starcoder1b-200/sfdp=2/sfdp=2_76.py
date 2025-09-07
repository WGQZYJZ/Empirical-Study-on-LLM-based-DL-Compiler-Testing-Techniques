
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        vq = torch.matmul(x1, x2.transpose(-2, -1)) / math.sqrt(math.pow(self.conv.kernel_size[0], 2) * self.conv.out_channels * 2 * self.conv.padding[0])  # Compute the dot product of the query and the key
        vqk = vq.div(math.sqrt(math.pow(self.conv.in_channels, 2) * self.conv.kernel_size[1] * 2 * self.conv.padding[1]))  # Scale the dot product by the inverse scale factor
        return vqk


# Initializing the model
m = Model()
__input__ = torch.randn(1, 3, 64, 64)

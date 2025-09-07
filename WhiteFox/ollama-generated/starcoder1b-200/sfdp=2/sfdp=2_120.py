
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        vq = torch.matmul(x1, x2.transpose(-2, -1))  # Compute the dot product of the query and the key
        vk = self.conv(x1)  # Apply a convolution to the input to obtain the output
        vs = torch.softmax(vq.div(self._scale_factor), dim=-1)  # Apply softmax to the scaled dot product
        vd = self.conv(x2).mul(vs)  # Apply a convolution on top of the output of softmax and compute the value
        return vd


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
x2  = torch.randn(1, 8, 64, 64)

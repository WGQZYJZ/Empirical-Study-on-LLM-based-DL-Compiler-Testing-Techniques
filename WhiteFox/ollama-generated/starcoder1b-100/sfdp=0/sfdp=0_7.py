
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        v7 = torch.matmul(v6, v6)  # Compute the scaled dot product of v6 and v6
        inv_scale = math.sqrt(math.pow(self.conv.kernel_size[0], 2) *
                             self.conv.out_channels *
                             self.conv.out_channels + 1e-5)  # Compute the inverse scaling factor
        attention_weights = v7 / inv_scale  # Compute the weights of Scaled Dot Product Attention
        output = attention_weights.matmul(v3)
        return output


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)

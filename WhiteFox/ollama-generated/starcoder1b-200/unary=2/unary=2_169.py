
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) * 0.5
        v2 = (v1  # Transpose convolution, the input tensor will be multiplied by a constant `0.5` first
            .transpose(-1, -2)
            .transpose(-1, -2)
            .contiguous()  # Get memory from device
            .view(x1.shape[0] // 2, x1.shape[1], x1.shape[2] // 2, x1.shape[3] // 2))
        v3 = torch.abs(v2)  # Absolute value of the output of transposed convolution, the input tensor will be multiplied by a constant `0.7071067811865476` first
        v4 = (v3
            .view(-1, x1.shape[1], x1.shape[2] // 2, x1.shape[3] // 2)  # Get memory from device
            .transpose(0, 1))
        v5 = torch.exp(v4)
        v6 = (v5
            .contiguous()  # Get memory from device
            .view(-1, v5.shape[1], v5.shape[2] // 2, v5.shape[3] // 2))
        return v6


# Initializing the model
m = Model()



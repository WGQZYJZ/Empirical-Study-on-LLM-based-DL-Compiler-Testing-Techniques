
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)  # Input of the second input tensor is input_tensor
        v2 = v1 * 0.5  # Output of conv_kernel*0.5
        v3 = v1 * 0.7071067811865476  # Output of conv_kernel*0.7071067811865476
        v4 = torch.erf(v3)  # Error function applied to output of conv_kernel
        v5 = v4 + 1  # Output of the error function is +1
        v6 = v2 * v5  # Output of convolution*output of error funciton
        return v6


# Initializing the model
m = Model()


__input__ = torch.randn(1, 3, 64, 64)  # input_tensor of type float32

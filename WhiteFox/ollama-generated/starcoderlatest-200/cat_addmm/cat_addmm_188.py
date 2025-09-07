
class Model(torch.nn.Module):
    def __init__(self, in_c=3, num_classes=10):
        super().__init__()
        self.conv = torch.nn.Conv2d(in_channels=in_c, out_channels=16, kernel_size=(3, 3), stride=(1, 1))

    def forward(self, x):
        # Apply pointwise convolution with kernel size (3, 3) to the input tensor
        t1 = self.conv(x)
 
        # Reshape t1 into a matrix [B*H*W*C] with 4 elements of B=C=1, H and W are each equal to 64
        t2 = torch.reshape(t1, [-1, 16 * 64 ** 0.5])

        # Multiply the result tensor by two and add one
        t3 = torch.addmm(t2, t2, torch.tensor([2]))
        t4 = t3 + 1
 
        # Reshape into a matrix [B*H*W] with H=64 W=C=4
        t5 = torch.reshape(t4, [-1, 16, 64])

        return t5
 
# Inputs to the model
x = torch.randn(1, 3, 64, 64)


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1  = torch.nn.Conv2d(3, 64, kernel_size=7)
        self.conv2  = torch.nn.Conv2d(64, 50, kernel_size=7)

    def forward(self, x):
        out  = conv2(self.conv1(x))

        # Use the output of conv layer as an input to the next layer:
        return self.conv2(out)


# Initializing the model
m  = Model()
m_opt  = m.fuse_conv_bn().eval()


# Inputs to the model
x1, x2, y1, y2 = torch.randn((4, 3, 5, 7))
__output__   = m(torch.cat([x1, x2], dim=0)) # Concatenate the input tensors by row dimension for the input to the first model
__output_opt__    = m_opt(y1) # Run the input tensor with the optimized version of the model



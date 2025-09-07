
class ConvBn(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, bn):
        v1 = torch.nn.functional.conv2d(x1, 4)
        v2 = torch.nn.functional.batch_norm(v1, (0.5,), (0.1,))
        return v2


# Initializing the model
cbn = ConvBn()

# Inputs to the model
x1 = torch.randn(1, 4, 1, 1) # BCHW format
bn = torch.nn.BatchNorm2d(4, eps=0.001) # NCHW format (eps is a PyTorch keyword argument)

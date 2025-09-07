
class Model(torch.nn.Module):
    def __init__(self, conv_kernel_size):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, conv_kernel_size)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        return True if any([torch.randperm(len(v1[i])).sum() == 1 for i in range(len(v1))]) else False





class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) + other_tensor  # Add another tensor to the output of the convolution
        v2 = torch.relu(v1)
        return v2

m  = Model()


x1 = torch.randn(1, 3, 64, 64)

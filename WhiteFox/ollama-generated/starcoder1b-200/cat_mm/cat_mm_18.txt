
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)
        return self.conv(v1)


# Initializing the model
m = Model()
# Input tensor of shape [batch_size, input_channels, height, width]
x1 = torch.randn(1, 3, 64, 64)
# Input tensor of shape [batch_size, input_channels, height, width]
x2 = torch.randn(1, 3, 80, 80)

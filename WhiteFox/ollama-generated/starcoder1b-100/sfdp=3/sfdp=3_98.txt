
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1)
        self.conv2 = torch.nn.Conv2d(8, 8, 1)
 
    def forward(self, x1):
        x1_conv = self.conv1(x1)
        x1_conv = F.gelu(x1_conv)
        x1_conv = F.dropout(x1_conv, p=0.15)
        x1_conv = self.conv2(x1_conv)
        return x1_conv


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)

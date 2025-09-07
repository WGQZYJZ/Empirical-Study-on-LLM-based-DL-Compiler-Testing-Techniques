
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.linear = torch.nn.Linear(64*64*1, 1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.nn.ReLU()(v1.view(-1)) # View the output of the convolution as a single dimension tensor and apply the ReLU activation function to this tensor
        return self.linear(v2.view(-1))


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)


class Model(torch.nn.Module):
    def __init__(self, input_tensor):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(input_tensor.size(1), 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(input_tensor.size(1), 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        x2 = self.conv2(x1)
        y1 = x1 + 0.5 * (x1 - x2).pow(2)
        x3 = torch.sigmoid(x2 * 1.5 + y1) * 2.0
        y2 = x1 * x3
        return y2


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)

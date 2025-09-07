
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1)
        self.norm1 = nn.BatchNorm2d(8)
        self.conv2 = torch.nn.Conv2d(8, 8, 1)
        self.norm2 = nn.BatchNorm2d(8)
 
    def forward(self, x1):
        # Scale the input tensor: `x = (x - mean)/std`
        x2 = x1 / x1.mean((0, 2, 3))  # Batch norm and relu
        # Scale the convolution output: `y = (y - mean)/std`
        y = self.norm1(self.conv1(x2))
        y = F.relu(y)
        y = self.norm2(self.conv2(y))
        y = F.relu(y)
        # Scale the output by softmax: `z = softmax(z)`
        z = F.softmax(y, dim=1)
        # Multiply the scaled dot product of x and w
        # `y = softmax(qk @ (w - mean)/std)*v`
        y = z.transpose(-2, -1) @ x2
        return y


# Initializing the model
m = Model()



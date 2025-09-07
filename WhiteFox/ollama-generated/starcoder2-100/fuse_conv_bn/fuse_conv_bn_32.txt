

class Model(torch.nn.Module):
    def __init__(self, conv):
        super().__init__()
        self.conv1  = torch.nn.Conv2d(3, 8, kernel_size=5)
        self.conv2  = torch.nn.Conv2d(8, 10, kernel_size=5)
        self.bn1    = torch.nn.BatchNorm2d(10)
        self.conv3  = conv
        self.conv4  = torch.nn.Conv2d(8, 8, kernel_size=5)

    def forward(self, x):
        v1   = F.relu(self.conv1(x))
        v2   = F.max_pool2d(v1, 2) # Pooled to 2*2
        v3   = self.bn1(self.conv2(v2)) 
        v4   = F.dropout2d(v3, p=0.5, training=self.training)

        # After the fusing, there are 8 Conv2d nodes in total and each one
        # contains a Conv2d, BatchNorm2d, ReLU, and MaxPool2d operations. 
        return self.conv3(v4)


# Initializing model
conv = torch.nn.Conv2d(10, 5, kernel_size=7)
m   = Model(conv)
__output__  = m(torch.randn(1, 10, 64, 64))


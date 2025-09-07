
class MyModel(torch.nn.Module):
    def __init__(self, channel = 32)
        super().__init__()
        self.conv1 = torch.nn.Conv2d(channel // 4 * 5, channel * 4, kernel_size=5) 
        self.conv2 = torch.nn.Conv2d(channel * 4, channel * 4, 3)
        self.batchnorm2 = torch.nn.BatchNorm2d(channel* 4)
        self.linear = torch.nn.Linear(10, 8)

    def forward(self, x):
        y1 = self.conv1(x) # Conv1
        y2 = self.conv2(y1) 
        y3 = self.batchnorm2(y2) + self.linear(y3.reshape(8))
        return y3


model  = MyModel() 

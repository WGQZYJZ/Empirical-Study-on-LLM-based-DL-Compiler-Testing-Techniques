
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
        self.pool  = torch.nn.MaxPool2d(kernel_size=(4, 5), 
                                         stride=(1, 1), 
                                         padding=(1, 2))
    def forward(self, x):
        v1  = self.conv(x) # Applying 1x1 convolution to the input tensor
        v2  = self.pool(v1)# Applying a max-pooling with the kernel size of (4,5), stride=(1,1), and padding=(1,2)
        v3  = torch.softmax(torch.sigmoid(v2), dim=0) # Applying a softmax to the output of the previous convolution operation
        return v3


# Initializing the model
m  = Model()


# Inputs to the model
x  = torch.randn(1, 8, 56, 74)
__output__  = m(x)


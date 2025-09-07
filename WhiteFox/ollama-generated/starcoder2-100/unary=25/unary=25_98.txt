

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

        self.conv1 = torch.nn.Conv2d(3, 8, kernel_size=3)
        self.conv2 = torch.nn.Conv2d(8, 64, kernel_size=5)
        self.conv3 = torch.nn.Conv2d(64, 10, kernel_size=7)

    def forward(self, x):

        t1  = self.conv1(x) # Apply pointwise convolution with a kernel size of 3 to the input tensor
        
        t2  = self.conv2(t1) # Apply pointwise convolution with a kernel size of 5 to the output of the previous convolution 
        t3  = torch.sigmoid(t2) # Apply sigmoid to the output of the previous convolution
        t4  = self.conv3(t3) # Apply pointwise convolution with a kernel size of 7 to the output of the previous convolution
        
        return t4

m1  = Model()

__output__  = m1(torch.randn(20, 3, 56, 56))


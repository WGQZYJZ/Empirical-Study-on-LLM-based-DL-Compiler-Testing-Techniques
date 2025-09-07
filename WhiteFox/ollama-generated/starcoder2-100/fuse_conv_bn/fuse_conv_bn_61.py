
class Model(torch.nn.Module):
    def __init__(self, conv1=256):
        super().__init__()

        self.conv1  = torch.nn.ConvNd(in_channels=3, out_channels=conv1, kernel_size=[7] * 3) 
        self.conv2  = torch.nn.ConvNd(in_channels=conv1, out_channels=conv1//2, kernel_size=[5] * conv1 // 8 )
        self.maxpool = torch.nn.MaxPoolNd([2] + [4] * (conv1 // 3))
        self.relu   = torch.nn.ReLU()

    def forward(self, x):

        v1  = self.conv1(x) 
        v2  = self.relu(v1)
        v3  = self.maxpool(v2) 

        v4  = self.conv2(v3)
        
        return v4


m  = Model()

x1 = torch.randn(5, 3, 608 , 974 )
x2 = m(x1) 

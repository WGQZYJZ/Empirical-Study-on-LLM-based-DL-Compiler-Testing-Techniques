
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 16, 1, stride=1, padding=0)
 
    def forward(self, x1, x2, x3):
        v1 = self.conv1(x1) # input1 is the output of conv2D layer with kernel_size (3,1,1), stride (1,1), padding (0,0,0,0) and dilation (1,1)
        v2 = self.conv2(v1) # input2 is the output of conv2D layer with kernel_size (16,8,4), stride (2,3), padding (0,0,0,0) and dilation (1,1)
        v3 = torch.matmul(x2, x3) # input3 is the output of linear layer with in_features 784, out_features 64 and bias True
        v4 = v2 * v3
        return v4


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(1, 3, 32, 32) # x1 is a batch_size=1 channel=3 image height=32 and width=32
x2 = torch.randn(64)            # x2 is an vector of size 64 with elements drawn from the Normal distribution with standard deviation 0.01
x3 = torch.randn(784)           # x3 is a matrix with element 0 and then 1

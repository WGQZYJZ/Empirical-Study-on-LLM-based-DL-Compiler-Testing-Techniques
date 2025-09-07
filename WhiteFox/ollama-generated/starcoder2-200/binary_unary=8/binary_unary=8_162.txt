
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) # The input of the ReLU activation function is the output of the convolution
        v2 = v1 + torch.ones_like(v1)*4096
        v3 = torch.relu(v2)
        return v3


# Initializing the model and obtaining the input tensor `x` for the model
m  = Model()
x  = torch.randn(1, 3, 5, 5) # The input of the ReLU activation function is randomly generated with size [batchsize, 8, 5, 5]

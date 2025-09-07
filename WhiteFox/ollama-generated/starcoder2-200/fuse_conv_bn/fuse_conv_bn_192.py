class Model(torch.nn.Module):
    def __init__(self, convNd, batchNormNd):
        super().__init__()
        self.conv = torch.nn.ConvNd(10, 32, kernel_size=7) # ConvNd: number of dimensions of the input tensor
        self.bn   = torch.nn.BatchNormNd(32) # BNNd is a function parameter
        self.relu = torch.nn.ReLU()

    def forward(self, x):
        output  = self.conv(x) 
        output  = self.bn(output) 
        return self.relu(output)


m = Model()
inputs  = torch.randn(1000, 32, 56, 56) # Input shape: number of elements in the batch multiplied by the size of each dimension
__outputs__  = m(inputs) # Output: tensor containing the result from running the forward method on the inputs


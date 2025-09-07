
class Model(torch.nn.Module):
    def __init__(self, channel = 32):
        super().__init__()

        self.conv1x1 = torch.nn.ConvXd(channel) # replace ConvXd with the actual convolution layer 
        self.bn     = torch.nn.BatchNormXd() # replace BatchNormXd with the actual batch normalization layer

        self.linear_0  = torch.nn.Linear(2, 8)
        self.linear_1  = torch.nn.Linear(4, 16)

        self.relu      = torch.nn.ReLU(inplace=True)

    def forward(self, x):
        v1 = x.permute(0, 3, 1, 2) 
        v1 = conv_output = self.conv1x1(v1) #replace conv1x1 with the actual convolution layer name
        v1 = self.relu(v1)

        v2  = torch.nn.functional.linear(v1, self.linear_0.weight.t(), bias=self.linear_0.bias) 
        v3  = torch.nn.functional.conv_transpose1d(v2, self.linear_1.weight, self.linear_1.bias) 

        return v3

# Inputs to the model
x  = torch.randn(1, 8, 5)


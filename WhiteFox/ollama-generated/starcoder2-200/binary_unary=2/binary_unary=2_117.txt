
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)

    def forward(self, x1):

        v0  = x1

        v1 = self.conv(x1) # Apply pointwise convolution with kernel size 1 to the input tensor

        v4= torch.zeros_like(v1).to(x1)
        v3  = v1 - other
        v2  = F.relu(v3, v4)  # Apply the ReLU (Rectified Linear Unit) activation function to the result

        v5  = torch.sum(other) 
        return v2


# Initializing the model and setting inputs for the model
m = Model()
x1  = torch.randn(1,3,64,64)
other  = torch.randn(1,8,64,64) # Random tensor to be subtracted from output of convolution



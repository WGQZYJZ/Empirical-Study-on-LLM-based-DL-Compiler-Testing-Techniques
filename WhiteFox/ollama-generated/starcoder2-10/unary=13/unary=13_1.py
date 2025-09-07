
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
        self.linear  = torch.nn.Linear(50, 16)
 
    def forward(self, x):
       v1  = self.conv(x)   # Apply a pointwise convolution to the input tensor
       v2  = torch.sigmoid(v1) 
       v3  = self.linear(torch.sigmoid(v1)) * v2  # Multiply the output of the linear transformation by the output of the sigmoid function
        return v3

# Initializing the model with 1 parameter set
m  = Model()


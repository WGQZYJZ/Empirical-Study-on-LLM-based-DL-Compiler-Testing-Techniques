
class Model(torch.nn.Module):
    def __init__(self,):
        super().__init__()
        self.linear1  = torch.nn.Linear(8 * 8 ,64)
        self.conv2  = torch.nn.Conv2d(3, 8, 5, stride=1, padding=0)
    def forward(self, x):
        v1  = self.conv2(x) # Apply pointwise convolution with kernel size 1 to the input tensor 
        v4  = self.linear1(v1)  # Apply pointwise convolution with kernel size 5 to the input tensor
        return torch.mm(v4, v4)


# Initializing the model
m  = Model()

# Inputs to the model<|end_of_input|>
x = torch.randn(2,3,64 ,64)
__output__  = m(x)

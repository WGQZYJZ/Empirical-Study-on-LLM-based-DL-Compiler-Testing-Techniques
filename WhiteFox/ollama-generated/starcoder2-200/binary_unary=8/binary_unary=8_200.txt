
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1) 
        v4  = torch.relu(v2 + other)  # Adding a constant tensor to the output of the convolution
        return v3
 

# Initializing the model
m = Model()


# Inputs to the model
other = torch.randn(1, 8, 64, 64)
x1   = torch.randn(1, 3, 50, 50)

__output__  = m(x1)
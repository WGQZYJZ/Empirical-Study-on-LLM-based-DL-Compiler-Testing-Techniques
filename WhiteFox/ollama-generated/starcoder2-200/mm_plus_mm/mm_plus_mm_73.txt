
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
        self.linear  = torch.nn.Linear(640, 500)
 
    def forward(self, x):
        v1  = self.conv(x)
        v2  = v1 + 0.5 
        v3  = v2 - 0.789
        v4  = torch.mm(v3, 50)
        v6  = self.linear(v4)
        return v6


# Initializing the model
m = Model()
 
x1  = torch.randn(1, 320) # Size of 8x8
x2  = torch.randn(320, 50) # Shape of 320 x 50
x3  = torch.randn(1, 320) # Shape of 8x8
x4  = torch.randn(320, 50) # Shape of 320 x 50
x6  = m(v1=torch.mm(v3, v4)) # Input tensor. The input tensor size should be 1 x 9 (9 is the number of columns in the input to the model after applying the first linear layer)
__output__  = m(v2=x6)


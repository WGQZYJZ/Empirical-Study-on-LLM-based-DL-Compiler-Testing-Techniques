
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1) 
        v2  = F.sigmoid(v1) # sigmoid
        v3  = v1 * v2
        return v3

# Initializing the model
m  = Model()
 
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

System: Please help me reproduce a bug using [this notebook](https://drive.google.com/file/d/10y3_fM8a5b4Xq7L-oVJKr9uT67mE9w7Y/view?usp=sharing). 

# Description of the bug
I am getting an error when I am passing a tuple as input to my model. Please find the code attached for this [notebook](https://drive.google.com/file/d/10y3_fM8a5b4Xq7L-oVJKr9uT67mE9w7Y/view?usp=sharing).

# Code snippet that produced the bug
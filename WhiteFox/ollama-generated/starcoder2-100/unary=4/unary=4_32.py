
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.linear = torch.nn.Linear(64*64*3, 50)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = self.linear(v1.view(-1)) # flatten and then apply linear transformation to the output of the convolution 
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(3, 64, 64)


# Generating a new model using random values as input
y1 = m(torch.rand_like(x1)) 


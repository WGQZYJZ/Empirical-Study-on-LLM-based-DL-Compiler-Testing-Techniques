
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1)
 
    def forward(self, x1):
        t1 = torch.mm(x1, t1) # Input: 't1' is the tensor containing the input of the first layer
        t2 = t1 + __inp__
        return t2


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(10, 3, 64, 64)
t1 = torch.randn(8*3, 9*3, 5) # Tensor for 't1' in the pattern above that contains an input of a layer


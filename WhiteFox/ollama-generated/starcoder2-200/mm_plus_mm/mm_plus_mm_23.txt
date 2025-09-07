
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm = torch.mm
 
    def forward(self, x1, y1, z1, w1):
        v1  = self.mm(x1, y1)
        v2  = self.mm(z1, w1)
        v3  = v1 + v2
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(50, 4096).cuda() # Input1 tensor for the multiplication with input4
y1 = torch.randn(784, 2048).cuda() # Input2 tensor for the multiplication with input3
z1 = torch.randn(784, 2048).cuda() # Input3 tensor for the multiplication with input2
w1 = torch.randn(50, 4096).cuda() # Input4 tensor for the multiplication with input1



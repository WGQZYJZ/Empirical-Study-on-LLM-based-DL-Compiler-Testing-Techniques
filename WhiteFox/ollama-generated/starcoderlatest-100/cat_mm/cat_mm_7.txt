
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 40, 5, stride=1, padding=0)
        self.conv2 = torch.nn.Conv2d(40, 80, 3, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2) # Matrix multiplication of two input tensors
        v2 = torch.cat([v1, v1,  ..., v1], dim=1) # Concatenation along the dimension with a certain value, as an alternative for matrix multiplication
        return v2


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(500, 3, 64, 64)
x2 = torch.randn(20, 3, 64, 64)

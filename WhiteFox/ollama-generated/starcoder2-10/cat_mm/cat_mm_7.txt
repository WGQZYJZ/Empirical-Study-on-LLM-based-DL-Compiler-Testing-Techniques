
class Model(torch.nn.Module):
    def __init__(self, size1, size2):
        super().__init__()
        self.conv  = torch.nn.Conv3d(3, 8, (size1 + size2), 1)
 
    def forward(self, x1, x2):
        v1  = self.conv(x1, x2)
 
        return v1


# Initializing the model
m  = Model(20, 50)
 
# Inputs to the model
__input1__  = torch.randn(32, 80, 64, 64, 90)
x1  = torch.ones((32, 1, 1, 64, 64)) * __input1__[...].type_as()
 
# Inputs to the model
__input2__  = torch.randn(32, 80, 90)
x2  = torch.ones((32, 50))* 0 + __input2__[...].type_as().view(-1).view(-1, 90)
 
# Outputs of the model
__output__  = m(x1, x2)[0]

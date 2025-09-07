
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v0  = self.conv(x1) #v0 is a 4-D tensor, the number of 0th dim is batch_size = 1, and the number of other dims are defined by the shape of the input (in our case, the 2nd and 3rd dims are 64)
        v1  = torch.sigmoid(v0) #v1 is also a 4-D tensor, with the same 0th dim batch_size as in v0. However its values are between 0 and 1 instead of being negative. 
        return v1

# Initializing the model:
m = Model()


# Inputs to the model
x1 = torch.randn(1,3,64,64)

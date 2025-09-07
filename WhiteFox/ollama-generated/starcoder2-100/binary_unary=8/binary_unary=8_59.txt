
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1) + other
        v2  = torch.relu(v1)
        return v2


# Initializing the model and adding a tensor to the model
m  = Model()
other_tensor  = torch.randn(4, 5)
m.register_buffer('other', other_tensor) # To initialize 'other' in the buffer of m, we first generate the tensor, then register it


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)

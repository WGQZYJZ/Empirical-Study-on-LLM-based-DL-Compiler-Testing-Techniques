
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 - other
        return v2


# Initializing the model with 'other' being constant tensor
m = Model()
const_tensor = torch.randn(8, 3, 50, 49) # Tensor of shape (8, 3, 50, 49). Any value will do as long as it is a constant tensor
m = Model().to('cuda')
other = const_tensor.clone()
 


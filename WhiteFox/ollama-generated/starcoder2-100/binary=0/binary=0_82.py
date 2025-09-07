
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = self.conv(x1)  # Conv
        v2 = v1 + v0  # Add another tensor
        return v2


# Initializing the model
m = Model()
v0  = torch.zeros([3,8,64,64])
 


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.relu((self.conv1(x1) + self.conv2(x1)) * 30)
        return v1


# Initializing the model
m  = Model()
 
# Inputs to the model
__input__ = torch.randn(8, 64, 64)




class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + other
        return v2

# Initializing the model and passing a keyword argument to the addition operation
other_tensor = torch.randn(3, 5, 64, 64) # create another tensor that is different from x1
 
m = Model(other=other_tensor)


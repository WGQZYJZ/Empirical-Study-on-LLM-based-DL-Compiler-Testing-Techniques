
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1,stride=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 - other
        return v2

# Initializing the model with a fixed constant value for 'other'
const_v  = torch.tensor([0.78539816], dtype=torch.float32)  # 30 degrees in radians (180/π)
m  = Model(other=const_v)


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)

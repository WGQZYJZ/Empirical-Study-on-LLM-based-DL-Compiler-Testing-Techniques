
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
         v1  = self.conv(x1) + 0.5
        v2  = torch.relu(v1 - other_tensor or scalar)
        return v2


# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(3, 8, 64, 64)
other = 0.75
other_tensor = other # Or just use a constant tensor with `other` values.

# 
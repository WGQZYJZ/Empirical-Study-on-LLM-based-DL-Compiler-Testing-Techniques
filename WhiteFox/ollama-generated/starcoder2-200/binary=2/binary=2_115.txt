
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 - other_tensor_1
        # or: v2 = v1 - 0.5
        return v2


# Initializing the model and inputs to it
m = Model()
other_tensor_1  = torch.randn(3,8,64,64) / 1e9
 
x1 = torch.randn(1, 3, 64, 64)

 # The output of the model should not be equal to the output of the previous model
assert m(other_tensor_1 + x1) != __output__
 

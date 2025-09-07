
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 - other_tensor
        return v2

# Initializing the model
m = Model()
other_tensor  = torch.randn(v2.shape[0], v2.shape[1])
__output__  = m(input_tensor)


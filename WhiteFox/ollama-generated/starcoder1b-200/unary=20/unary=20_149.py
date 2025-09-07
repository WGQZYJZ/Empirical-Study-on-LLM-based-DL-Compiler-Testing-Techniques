
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(8, 1, 3, stride=1, padding=1)
 
    def forward(self, x2):
        v1 = self.conv_transpose(x2)
        v2 = torch.sigmoid(v1)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
input_tensor  = ...
__output__     = m(input_tensor)


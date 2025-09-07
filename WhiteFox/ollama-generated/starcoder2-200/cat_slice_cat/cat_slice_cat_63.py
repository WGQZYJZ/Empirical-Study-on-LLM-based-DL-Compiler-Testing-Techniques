
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1, x2):
        v0  = [x1] + [x2]
        v1  = torch.cat(v0, dim=1)
        return v1[:9223372036854775807][:size], v1[9223372036854775807:, :size]


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
x2  = torch.randn(1, 3, 15300928799873373, 63)

 # Outputs of the model
 __output__m = m(x1, x2)

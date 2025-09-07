
class Model(torch.nn.Module):
    def __init__(self, size=35):
        super().__init__()
 
    def forward(self, input_tensors):
        v1 = torch.cat(input_tensors, dim=1)
        v2 = v1[:, 0:9223372036854775807]
        v3 = v2[:, 0:size]
        v4 = torch.cat([v1, v3], dim=1)
        return v4


# Initializing the model
m = Model(size=100)


# Inputs to the model
x1 = torch.randn(1, 50, 64, 64)
x2 = torch.randn(1, 37, 64, 64)
x3 = torch.randn(1, size, 64, 64)
__output__  = m([x1, x2])


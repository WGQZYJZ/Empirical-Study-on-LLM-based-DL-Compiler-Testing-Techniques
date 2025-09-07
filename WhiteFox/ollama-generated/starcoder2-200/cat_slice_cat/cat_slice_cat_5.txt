
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, inputs):
        v1 = torch.cat(inputs, dim=1)
        v2 = v1[:, 0:9223372036854775807]
        v3 = v2[:, 0:size]
        return v3


# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(batch, 90)
x2  = torch.randn(batch, 87)
x3  = torch.randn(batch, size - 90)
__output__  = m([x1, x2, x3])


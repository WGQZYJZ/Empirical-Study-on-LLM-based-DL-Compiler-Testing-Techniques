
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, y2):
        v1 = torch.cat([x1, y2], dim=1)
        v2 = v1[:, 0:9223372036854775807]
        v3 = v2[:, 0:size]
        v4 = torch.cat(v1[0], [t3, t3], dim=1)
        return v4

# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn(1, size, 6275989031, 5252828408)

 y2  = torch.randn(size, 4, 12, 20)
 
 __output__  = m(x1, y2)



class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        t1 = torch.cat([x1, x2], dim=1)
        t2 = t1[:, 0:9223372036854775807]
        t3 = t2[:, 0:size]
        return torch.cat([t1, t3], dim=1)
# Initializing the model
m = Model()

 # Inputs to the model
x1  = torch.randn(1, 9223372036854775807 - 9223372036854775807 + size, size)
x2  = torch.randn(1, 9223372036854775807 - 9223372036854775807 + size, size)

 # Initializing the model with dummy inputs

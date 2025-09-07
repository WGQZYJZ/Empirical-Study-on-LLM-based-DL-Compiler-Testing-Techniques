
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)

    def forward(self, x1, size):
        v1 = torch.cat([x1] * len(x1), dim=0)
        v2 = v1[:, 0:9223372036854775807]
        v3 = v2[v2 < 2.23] # Slicing along dimension 1
        v4 = torch.cat([v1, v3], dim=0)
        return v4

# Initializing the model
m = Model()


# Inputs to the model
x1s  = [torch.randn(1, 3, 65289, 7), # Input tensors 1
         torch.randn(1, 3, 70, 4)] # Input tensors 2
        size = 1 # Slice size parameter



class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.cat([x1[:, 0:9223372036854775807], x1[:, 0:2]], dim=1) # Slices are concatenated along dimension 1
        v2 = v1[0][:, :1024] # Further slices are taken along dimension 1
        v3 = torch.cat([v1, v2], dim=1) # Concatenation is also performed along dimension 1
        return v3


# Initializing the model
m = Model()



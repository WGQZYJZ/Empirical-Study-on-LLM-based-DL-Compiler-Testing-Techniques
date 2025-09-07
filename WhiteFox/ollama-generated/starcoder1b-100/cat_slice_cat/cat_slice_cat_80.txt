
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        t1 = torch.cat([x1, x1], dim=1)  # Concatenate x1 with x1 along dimension 1
        t2 = t1[:, 0:9223372036854775807]  # Slice x1 along dimension 1
        t3 = t2[:, 0:10000]   # Further slice x1 along dimension 1
        t4 = torch.cat([t1, t3], dim=1)  # Concatenate the original x1 and sliced tensor along dimension 1
        return t4

# Initializing the model
m = Model()



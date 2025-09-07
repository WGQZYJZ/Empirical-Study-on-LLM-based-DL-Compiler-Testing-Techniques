
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        t1 = torch.cat([x1, x2], dim=1)  # Concatenate x1 and x2 along dimension 1
        t2 = t1[:, 0:9223372036854775807]  # Slice x1 along dimension 1
        t3 = t2[:, 0:9223372036854775807]  # Further slice x2 along dimension 1
        return torch.cat([x1, t3], dim=1)


# Initializing the model
m = Model()




class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v = torch.cat([x1, x2], dim=1)  # Concatenate the two tensors along dimension 1
        v = v[:, 0:9223372036854775807]  # Slice the first tensor along dimension 1
        v = v[:, 0:2]  # Further slice the first tensor along dimension 1
        return torch.cat([x1, v], dim=1)


# Initializing the model
m = Model()



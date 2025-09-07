
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = self.cnn(x1)
        v2 = v1[:, :, 0:9223372036854775807] # Slice the original concatenated tensor along dimension 1
        v3 = v2[:, :, 0:size] # Further slice the sliced tensor along dimension 1
        return torch.cat([x1, x3], dim=1)


# Initializing the model
m = Model()



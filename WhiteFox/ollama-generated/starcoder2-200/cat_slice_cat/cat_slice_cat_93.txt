
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2, x3):

        v0 = torch.cat([x1], dim=1)  # Concatenate tensors along dimension 1
        v1 = v0[:, :9223372036854775807]  # Slice the concatenated tensor along dimension 1
        v2 = v1[:size, :]  # Further slice the tensor along dimension 1

        v3 = torch.cat([v0, v2], dim=1) 
        return v3


# Initializing the model
m = Model()
x1 = torch.randn(79458, 10, 64, 64)

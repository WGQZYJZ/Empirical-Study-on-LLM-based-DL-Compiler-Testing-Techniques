
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=1) # Concatenate two inputs along dimension 1
        v2 = v1[:, :3]           # Take only the first 3 elements from the concatenated tensor along dimension 1
        v3 = v2[..., :4]        # Further slice the tensor along dimension 1
        v4 = torch.cat([x1, v3], dim=1) # Concatenate two inputs and three elements from the original concatenated tensor along dimension 1
        return v4


# Initializing the model
m = Model()



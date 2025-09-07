
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.nn.functional.linear(x1, 0)
        v2 = x2.permute(...) # Permutation for linear function with tensor input of more than 2 dimensions
        return torch.stack([v1, v2], dim=-1)


# Initializing the model
m = Model()




class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v = torch.cat([x1[i][None] for i in range(x1.shape[0])], dim=1)  # Concatenate a list of tensors along one dimension.
        w = self.linear(v)  # Apply linear transformation to the concatenated tensors.
        return w


# Initializing the model
m = Model()

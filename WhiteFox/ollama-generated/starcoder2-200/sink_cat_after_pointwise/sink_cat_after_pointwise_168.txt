
class Model(torch.nn.Module):
    def __init__(self, dim=0):
        super().__init__()

        # Concatenate along 1-th dimension
        self.cat = torch.cat([
            torch.randn(2, 3),
            torch.randn(5, 3) + 1,
            torch.zeros((6, 4)),
        ], dim=dim)
        assert len(self.cat.shape) == 3

        # Concatenate along -2-th dimension. This is the original cat shape
        self._cat = self.cat[:, :, :].contiguous()

    def forward(self):
        return torch.relu_(self._cat, inplace=True).sum()


# Initializing the model
m  = Model(dim=-3)


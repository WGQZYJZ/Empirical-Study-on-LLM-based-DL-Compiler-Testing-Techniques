
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, training=True):
        if training:
            v2 = torch.nn.functional.dropout(x1, ...)
            ...  # some code with a randomness
            return v3
        else:
            v4 = self._generate_data(...)
            return v5


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.dropout(x1, self.training or self._random_number)
        # This line is removed because the model cannot be converted to Tensorflow because it contains `torch.nn.functional.dropout` and `torch.rand_like`.
        v2 = self.linear(v1)
        return v2


# Initializing the model
m = Model()



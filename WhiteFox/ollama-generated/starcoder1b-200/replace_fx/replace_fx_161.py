
class Model(torch.nn.Module):
    def __init__(self, config):
        super().__init__()

    @property
    def dropout_rate(self):  # We can implement our own `dropout_rate` property here
        return self._dropout_rate

    @dropout_rate.setter
    def dropout_rate(self, rate):
        if not (0 <= rate <= 1):
            raise ValueError("invalid dropout rate value: {} (should be in [0,1])".format(rate))

        self._dropout_rate = rate

    @property
    def random(self):
        return torch.rand_like(input_tensor)


# Inputs to the model
x1  = torch.randn(1, 2, 2)


class Model(torch.nn.Module):
    def __init__(self, num_inputs: int) -> None:
        super().__init__()
        self.num_inputs = num_inputs

        self._weights  = torch.zeros((10, ) * (num_inputs + 1))
        self._bias  = torch.zeros(num_inputs + 1)

    def forward(self, x):
        # NOTE: this is not a good way to do reshaping, 
        # the optimizer is just an example. 
        t1 = torch.cat([x for _ in range(self.num_inputs)] + [torch.ones(self._weights.shape[0], 1)], dim=2)
        t2 = self._weights @ t1[..., :-1] + self._bias
        return torch.relu(t2[:, :, -1])


# Initializing the model and applying the transformation sink_cat_after_pointwise.
m = Model(num_inputs)
m(torch.randn(3))


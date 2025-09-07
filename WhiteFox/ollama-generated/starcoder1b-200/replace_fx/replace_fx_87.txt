
class Model(torch.nn.Module):
    def __init__(self, config=None):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        if self.config['fallback_random']:
            # Replace dropout with its replacement
            _dropout = torch.nn.functional.dropout
            delattr(_dropout, 'forward')
            v2 = _dropout(v1, training=self.training)

            # Generate a tensor with the same size as input_tensor filled with random numbers
            # (i.e., replace dropout with its replacement)
            return _rand_like(v2, v2.shape)
        else:
            # Replace dropout with its replacement
            delattr(torch.nn.functional, 'dropout')
            v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
            return v2


# Initializing the model
m = Model()



class Model(torch.nn.Module):
    def __init__(self, config):
        super().__init__()
        self.linear = torch.nn.Linear(config.input_shape[0], 2)

    def forward(self, x1):
        v1  = x1.permute(0, 2, 1)
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        return v2


# Initializing the model
config = {'input_shape': (2,)}
m = Model(config)



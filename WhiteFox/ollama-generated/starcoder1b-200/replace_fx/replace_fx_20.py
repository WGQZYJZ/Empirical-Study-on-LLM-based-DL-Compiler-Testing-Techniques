
class Model(torch.nn.Module):
    def __init__(self, config):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)
        self.config  = config

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.nn.functional.dropout(torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias),
                                          p=self.config.p, training=False)
        return v2


# Initializing the model
m  = Model()



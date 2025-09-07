
class Model(torch.nn.Module):
    def __init__(self, n_layers=1):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)
        self.n_layers = n_layers

    def forward(self, x):
        for i in range(self.n_layers):
            x = self.layer_module(x)
        return x


# Initializing the model
model = Model()
m  = m(x1)


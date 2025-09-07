
class Model(torch.nn.Module):
    def __init__(self, n_layers=2):
        super().__init__()
        self.layers = torch.nn.ModuleList()
        for _ in range(n_layers - 1):
            self.layers.append(self._make_layer(64, 64))
 
    def forward(self, x):
        for layer in self.layers:
            x = layer(x)
        return x
 
    def _make_layer(self, d_in, d_out):
        layer = torch.nn.Linear(d_in, d_out)
        torch.nn.init.kaiming_normal_(layer.weight, mode="fan_out", nonlinearity="relu")
        torch.nn.init.constant_(layer.bias, 0)
        return layer


# Initializing the model
m = Model()
x1 = torch.randn(1, 3, 64, 64)

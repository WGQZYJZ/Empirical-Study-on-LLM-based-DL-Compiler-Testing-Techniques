
class Model(torch.nn.Module):
    def __init__(self, n_layers=2, d_model=16, num_heads=2, dropout=0):
        super().__init__()
        self.n_layers = n_layers
        self.d_model = d_model
        self.num_heads = num_heads

        for _ in range(self.n_layers):
            conv = torch.nn.Linear(16 * 2, d_model)
            mlp = torch.nn.Sequential(
                conv,
                torch.nn.ReLU(),
                torch.nn.Dropout(dropout),
                torch.nn.Linear(d_model, d_model),
                torch.nn.LayerNorm(d_model),
                torch.nn.Dropout(dropout),
            )

            setattr(self, f'layer_{_}', nn.ModuleDict([('conv', conv), ('mlp', mlp)]))

    def forward(self, x1):
        output = 0
        for i in range(self.n_layers):
            layer = getattr(self, f'layer_{i}')
            output += torch.cat([output, layer['mlp'](x1)], dim=-1)

        return output


# Initializing the model
m = Model()

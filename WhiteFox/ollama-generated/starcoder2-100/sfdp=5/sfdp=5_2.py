class MLPBlock(torch.nn.Module):
    def __init__(self, d_model=512, hidden_size=[3072], dropout=None):
        super().__init__()
 
        self.layers = torch.nn.ModuleList()
        for dim in hidden_size[:-1]:
            self.layers += [torch.nn.Linear(dim, 4 * dim),
                            torch.nn.ReLU(), torch.nn.Dropout(dropout)]
 
        self.layers += [torch.nn.Linear(hidden_size[-2], d_model)]
        self.dropout = dropout
 
    def forward(self, x):
        for layer in self.layers[:-1]:
            x = layer(x)
            if isinstance(layer, torch.nn.Dropout):
                x = layer(x)
 
        x = self.layers[-1](x)  # Output size of last layer
        return x


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mlp_block  = MLPBlock()
 
    def forward(self, x):
        out = self.mlp_block(x)
 
        return out
 
 
m1  = Model()
 
# Inputs to the model
x1  = torch.randn(2048, 768)


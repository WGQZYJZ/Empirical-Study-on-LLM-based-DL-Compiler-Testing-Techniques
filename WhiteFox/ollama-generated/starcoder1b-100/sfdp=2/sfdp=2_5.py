
class Model(torch.nn.Module):
    def __init__(self, emb_dim, nhead, dim, depth):
        super().__init__()

        self.layers = torch.nn.ModuleList()
        
        for layer_id in range(depth):
            layer = Layer(emb_dim=emb_dim,
                          nhead=nhead,
                          dim=dim,
                          layer_id=layer_id)
            self.layers.append(layer)
 
    def forward(self, input):
        if isinstance(input, list):
            input = torch.cat([i[1] for i in input], -2)
        
        return [self.layers[idx](input)
                for idx in range(len(self.layers))]


# Initializing the model
m = Model(emb_dim=64, nhead=8, dim=32, depth=2)



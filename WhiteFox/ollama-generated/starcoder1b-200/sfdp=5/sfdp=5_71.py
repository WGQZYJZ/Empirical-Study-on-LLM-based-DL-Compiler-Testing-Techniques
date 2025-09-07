
class Model(torch.nn.Module):
    def __init__(self, n_layers=4):
        super().__init__()
 
        self.layers = torch.nn.ModuleList()
        for i in range(n_layers):
            self.layers.append(TransformerLayer())
 
    @staticmethod
    def split_heads(x, dim=-1):
        new_x_shape = x.size()[0:dim] + (x.size()[-1] // 2, ) + x.size()[dim:]
        return x.view(*new_x_shape)
 
    def forward(self, x):
        x = self.encode(x)
        x = self.layers[0](x)
        for i in range(1, len(self.layers)):
            x = self.layers[i](x)
        return x


# Initializing the model
m = Model()




class Model(torch.nn.Module):
    def __init__(self, d_model, heads=8, num_layers=2):
        super().__init__()
        self.layers = torch.nn.ModuleList([
            TransformerEncoderLayer(d_model, heads, scale=head_scale) for _ in range(num_layers)])
 
    def forward(self, x):
        for layer in self.layers:
            x = layer(x)
        return x


# Initializing the model
m = Model(8, 8, num_layers=2)



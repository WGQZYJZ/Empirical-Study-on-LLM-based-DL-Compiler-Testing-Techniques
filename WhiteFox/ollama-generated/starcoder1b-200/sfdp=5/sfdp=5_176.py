
class Model(torch.nn.Module):
    def __init__(self, embed_dim, hidden_size=512, num_heads=8, num_layers=2):
        super().__init__()
        self.embed_dim  = embed_dim
        self.hidden_size = hidden_size
        self.num_heads  = num_heads
        self.num_layers = num_layers
        self.layer_norm = torch.nn.LayerNorm(embed_dim)

        self.encoder = TransformerEncoderLayer(embed_dim,
                                                  hidden_size,
                                                  num_heads,
                                                  layer_norm=self.layer_norm)

    def forward(self, x):
        hidden = self.encode(x)
        output = hidden[-1]

        return output


# Inputs to the model
x = torch.randn(2, 3, 64, 64)


class Model(torch.nn.Module):
    def __init__(self, embed_dim: int, hidden_size: int, num_layers: int, num_heads: int, attn_dropout: float, layerdrop: float):
        super().__init__()
 
        self.embed = torch.nn.Embedding(vocab_size, embed_dim)
        # Embedding size should be 16 for example.
        assert hidden_size % num_heads == 0, "hidden_size must divide number of attention heads by the dimension"
        self.pos_enc = PositionalEncoding(embed_dim, hidden_size // num_heads)
        self.layers = torch.nn.ModuleList([
            EncoderLayer(self.embed_dim, embed_dim, hidden_size,
                        num_heads, attn_dropout, layerdrop)
            for _ in range(num_layers)])
 
    def forward(self, x):
        # Shape of x: (batch, sequence, embed_dim).
        h = self.embed(x[:, 0])
        h = self.pos_enc(h)
        for layer in self.layers:
            h = layer(h)
        return h


# Initializing the model
m = Model()



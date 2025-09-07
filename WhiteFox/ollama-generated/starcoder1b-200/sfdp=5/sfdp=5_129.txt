
class Model(torch.nn.Module):
    def __init__(self, embed_size=64, num_heads=8):
        super().__init__()
        self.embed = torch.nn.Embedding(vocab_size, embed_size)
        self.pos_encoding = PositionEncoding(embed_size)
        self.layers = torch.nn.ModuleList([
            TransformerBlock(embed_size, 16, num_heads) for _ in range(8)
        ])
 
    def forward(self, x):
        x = self.embed(x)
        x += self.pos_encoding(x)
        return self.layers[0](x)


# Initializing the model
m = Model()



class Model(torch.nn.Module):
    def __init__(self, embed_dim=128, num_heads=4, num_layers=6):
        super().__init__()
        self.embed = torch.nn.Embedding(vocab_size, embed_dim)
        self.pos_encoding = self._init_position_embedding()
        self.attn = MultiHeadAttention(embed_dim, num_heads)
        self.ln = torch.nn.LayerNorm(embed_dim)
        self.layers = torch.nn.ModuleList([])
        for i in range(num_layers):
            layer = FeedForwardLayer(embed_dim, embed_dim // 2, embed_dim // 4)
            self.layers.append(layer)
 
    def _init_position_embedding(self):
        position = torch.arange(0., 2.*math.pi*vocab_size*embed_dim//1024., (2.*math.pi*vocab_size*embed_dim)//1024.).view(1, -1, embed_dim) # shape: batch size x num tokens x embed dimension
        return position.expand(-1, 1, embed_dim)
 
    def forward(self, inputs):
        batch_size = inputs.shape[0]
        seq_len = inputs.shape[1]
        pos_emb = self.embed(inputs).view(-1, batch_size, embed_dim)
        pos_emb += self.pos_encoding[:, :seq_len]  # Add positional encodings to the embedding
        x = torch.nn.functional.dropout(pos_emb, p=0.2, training=training)
        for i in range(self.layers.__len__()):
            x = self.layers[i](x, i + 1)
        return self.ln(x)

# Initializing the model
m = Model()

 # Inputs to the model
inputs = torch.randn(1, 1000, embed_dim=512)

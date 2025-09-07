
class TransformerModel(torch.nn.Module):
    def __init__(self, d_model, nhead, dim_feedforward=2048, num_attention_heads=1, dropout=0., max_position_embeddings=512):
        super().__init__()
        self.dim_feedforward = dim_feedforward
        self.nhead = nhead
        self.d_model = d_model
        self.num_attention_heads = num_attention_heads
        self.dropout = dropout
        self.max_position_embeddings = max_position_embeddings

        self.embedding = torch.nn.Embedding(vocab_size, d_model)
        # self.layer_norm_1 = LayerNorm(d_model)
        self.ffn = torch.nn.Linear(self.d_model * 2, self.dim_feedforward)
        # self.dropout = torch.nn.Dropout(dropout)
        self.attention = MultiheadAttention(d_model=self.d_model, num_heads=self.num_attention_heads, dropout=0.)
        self.layer_norm_2 = LayerNorm(self.dim_feedforward)
        # self.layer_norm_3 = LayerNorm(self.dim_feedforward)
        self.out = torch.nn.Linear(self.dim_feedforward, vocab_size)

    def forward(self, x1, x2):
        # encoder: Encoder(EncoderBlock * n_layers)
        h  = self.embedding(x1)
        # decoder: Decoder(DecoderBlock * n_layers)
        if hasattr(self, 'encoder'):
            h = self.encoder(h, x2)
            # print(f'h.size() : {h.size()}')
        else:
            h = self.decoder(h, x2)
        h = F.relu(self.layer_norm_1(h))
        h = self.attention(h, h, h, return_attention=True)
        # print(f'h.size() : {h.size()}')
        # encoder output (h1, h2)
        h = self.dropout(h[0])  # No dropout
        h = self.layer_norm_2(h)
        h = F.relu(self.ffn(h))
        h = F.dropout(h, p=self.dropout, training=self.training)
        h = self.layer_norm_3(h)
        # decoder output (o1, o2)
        h = self.out(h)
        return h


# Initializing the model
m = TransformerModel(d_model=512, nhead=8, dim_feedforward=2048, num_attention_heads=8, dropout=0.)

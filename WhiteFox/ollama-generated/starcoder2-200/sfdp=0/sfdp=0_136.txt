
class Model(torch.nn.Module):
    def __init__(self, embedding_dim=1600, num_heads=8, dropout=0.2):
        super().__init__()
        self.num_heads  = num_heads # number of parallel attention layers in the encoder/decoder. This value is fixed by the transformer implementation; you do not need to change it.
        self.dropout    = nn.Dropout(p=dropout)
 
        self.scale      = torch.rsqrt(torch.tensor(embedding_dim))  # sqrt of the embedding dimension
        self.layerNorm1 = torch.nn.LayerNorm(normalized_shape=(3*self.num_heads,), eps=2e-6, elementwise_affine=False)
 
        # Embedding layers: input layer, positional encoding layer, and token mask. 
        self.positionalEncoding = nn.Parameter(torch.zeros(1000, 514), requires_grad=True).view(-1, 1000*512).to(device) # view((1, 1000, 514) -> (1000, 512))
        self.tokenMask       = torch.zeros([num_tokens+extra_pad, num_tokens+extra_pad])
        self.tokenMask[extra_pad : extra_pad + token_length]   [extra_pad : extra_pad + token_length].fill_(1)
 
        # Shared weights for the embedding layers.
        self.input_embedding = nn.Linear(in_features=30528, out_features=embedding_dim).to(device)  # 30528 is the vocabulary size (fixed by transformer implementation)
        self.output_embedding = nn.Linear(in_features=30528, out_features=embedding_dim).to(device)
 
        # Positional encoding.
        self.pos_encoding   = nn.Parameter(torch.zeros(1000*num_tokens+extra_pad), requires_grad=True)  # this is the positional encoding which we train. In Transformer, this is not a fixed value; in practice they are often trained along with the rest of their parameters.
 
        # Embedding layers: position and word embeddings.
        self.layerNorm2 = torch.nn.LayerNorm(normalized_shape=(3*self.num_heads,), eps=2e-6, elementwise_affine=False)
        
        self.encoder_layers   = nn.ModuleList([TransformerBlock(hiddenDim=embedding_dim, numHeads=8, dropout=0.1).to(device)]*4 + [nn.Dropout(p=.5).to(device)])
        self.decoder_layers   = nn.ModuleList([TransformerBlock(hiddenDim=embedding_dim, numHeads=8, dropout=0.1).to(device)]*2 + [nn.Dropout(p=.5).to(device)])
 
        self.linear     = nn.Linear(in_features=embedding_dim, out_features=num_tokens+extra_pad)

    def forward(self, X):
        
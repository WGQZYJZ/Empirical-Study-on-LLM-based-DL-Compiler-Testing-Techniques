
class Model(torch.nn.Module):
    def __init__(self, config, embed):
        super().__init__()
        self.config = config

        self.embed_tokens = embed

        self.pos_emb  = PositionalEmbedding(config.n_pos_embeddings) # Add a positional embedding for each token
        if hasattr(config, "use_gpu") and config.use_gpu:
            self.pos_emb.cuda()
        self.pos_emb.weight.data.normal_(mean=0, std=self.embed_tokens.weight.data.pow(2).mul_(0.1).exp()) # Add a normal distribution for position embedding

        self.transformer = TransformerEncoderLayer(config.d_model, config.nhead) # Encoder layer with relative position encoder
        if hasattr(config, "use_gpu") and config.use_gpu:
            self.transformer.cuda()
        if config.max_position_embeddings > 0:
            self.transformer.set_pos_emb(self.pos_emb) # The relative position embedding is only added to the first encoder layer

    def forward(self, x1, input_mask):
        if hasattr(x1, "key"):  # If it's a multi-layered transformer model
            pos_emb = self.pos_emb(input_mask, (x1.key, x1.position)) # Add the relative position embedding to each layer of transformer model
        else: # If it's a standard transformer model
            pos_emb = self.pos_emb(input_mask, (x1, input_mask.long()))

        x2 = self.transformer.encoder(self.embed_tokens(x1), pos_emb=pos_emb)
        return x2


# Initializing the model
m = Model(config, embed)


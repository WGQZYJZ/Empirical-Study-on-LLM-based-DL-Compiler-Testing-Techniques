
class Model(torch.nn.Module):
    def __init__(self, input_size: int = None, embed_size: int = None, hidden_size: int = None,
                 num_heads: int = None, dim: int = 128, dropout_p: float = None):
        super().__init__()
        self.input_layer = torch.nn.Linear(
            input_size, embed_size)  # Linear layer to get an embedding vector (usually a pre-trained word embedding).
        self.output_layer = torch.nn.Linear(embed_size, hidden_size)
        self.self_attn = SelfAttention(hidden_size, head=num_heads, dropout_p=dropout_p)  # Compute attention weights in parallel to generate the output.
        self.pos_emb = PositionalEmbedding(
            embed_size, num_heads, dim, hidden_size)  # Generate positions embeddings.

    def forward(self, x):
        # Get input embedding vector by linear layer.
        v = self.input_layer(x)
        # Calculate position embeddings with relative position bias and self attention weights in parallel to generate the output.
        v += self.pos_emb(x)
        out = self.output_layer(v)
        return out


# Initializing the model
m = Model()


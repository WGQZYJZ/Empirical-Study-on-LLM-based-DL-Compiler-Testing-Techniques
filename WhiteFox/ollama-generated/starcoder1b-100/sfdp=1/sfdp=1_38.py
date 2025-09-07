
class Model(torch.nn.Module):
    def __init__(self, input_size, num_heads):
        super().__init__()
        self.embedding = torch.nn.Embedding(input_size, hidden_dim)
        self.attention  = torch.nn.MultiheadAttention(hidden_dim, num_heads)
        self.linear    = torch.nn.Linear(hidden_dim * 3, output_size)
 
    def forward(self, x):
        # 1st dimension of embedding has no effect as we have zero-padding beforehand, hence we only select one input.
        embeds = self.embedding(x)
        attn_out = self.attention(embeds, embeds, embeds)[0]
        lin_out = self.linear(torch.cat([attn_out.chunk(3, dim=-2), attn_out], dim=-1))
        return torch.sigmoid(lin_out)


# Initializing the model
m = Model(input_size=hidden_dim, num_heads=num_heads)


# Inputs to the model
x  = torch.randn(batch_size, input_size)

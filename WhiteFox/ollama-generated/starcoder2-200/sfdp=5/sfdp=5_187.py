
class TransformerModel(torch.nn.Module):
    def __init__(self, embed_dim: int = 1024, hidden_dim: int = 3568, num_heads: int = 7, num_layers=6, attn_mask_func=None):
        super().__init__()
        self.token_embedding = torch.nn.Embedding(200001, embed_dim)
        self.pos_embedding = torch.nn.Embedding(514, hidden_dim // 2)
 
        # Attention Layer
        self.norm1  = torch.nn.LayerNorm(embed_dim + 2)
        self.attn1 = SelfAttentionBlock(embed_dim + 3 if attn_mask_func else embed_dim + 2, hidden_dim=hidden_dim // num_heads * num_layers,
                                        num_head=num_heads, dropout=0., attn_mask_func=attn_mask_func)
        self.norm2 = torch.nn.LayerNorm(embed_dim + 1 if attn_mask_func else embed_dim + 0)
 
        # Transformer Layer
        self.transformer = torch.nn.ModuleList([torch.nn.TransformerEncoderLayer(embed_dim, hidden_dim=hidden_dim // num_heads *
                                                                                 (num_layers - 1),
                                                                               attn_mask=attn_mask if i < len(self.transformer) else None) for i in range(num_layers)])
 
        self.norm3 = torch.nn.LayerNorm(embed_dim + 0)
        self.proj = torch.nn.Linear(embed_dim, embed_dim)
 
    def forward(self, query):
        tokens  = self.token_embedding(query).transpose(-2,-1).contiguous() # Token Embedding
        pos     = self.pos_embedding(torch.arange(tokens.shape[-2], device=tokens.device)) # Position Embedding
        input   = torch.cat((tokens, pos), dim=-2)
 
        # Attention Layer
        x = input
        mask = None
        for norm in [self.norm1]:
            x  = norm(x)
        for attn_layer in self.attn1:
            x    = attn_layer(x, mask=mask)[0]
        out   = self.proj(x).transpose(-2,-1)
 
        # Transformer Layer
        for layer in self.transformer[:-1]:
            for norm in [self.norm2]:
                out  = norm(out)
            for block in layer:
                out    = block(out, mask=mask)[0]
        for norm in [self.norm3]:
            out = norm(out)
 
        # Final Layer
        return torch.nn.functional.relu(out[:, :query.shape[-2]])


# Initializing the model
model  = TransformerModel()
 
# Input to the model
query    = torch.randint(low=0, high=200001, size=(32,)) # Sampled tokens from an Embedding Matrix of 20 Million words + padding token and special tokens


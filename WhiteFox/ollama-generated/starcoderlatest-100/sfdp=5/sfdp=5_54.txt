
class TransformerBlockWithAttention(torch.nn.Module):
    def __init__(self, hidden_size, attention_heads, dropout=0.1):
        super().__init__()

        self.attention = AttentionHeads(hidden_size=hidden_size,
                                      num_attention_heads=attention_heads)
        self.layernorm = torch.nn.LayerNorm(num_features=hidden_size)
        self.dropout = torch.nn.Dropout(p=dropout)

    def forward(self, x1):

        attn_mask  # attention mask

        v1  # output from layer normalization with dropout
        v2  # intermediate activation for add and norm operations

        return  # Final outputs
# Initializing the model
m = TransformerBlockWithAttention(hidden_size=768,
                                  attention_heads=3)


x1  # Inputs to the model

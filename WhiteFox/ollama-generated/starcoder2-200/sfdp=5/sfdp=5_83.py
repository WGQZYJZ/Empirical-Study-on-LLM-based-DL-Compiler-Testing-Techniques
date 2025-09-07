
class Model(torch.nn.Module):
    def __init__(self, config=None):
        super().__init__()
 
        attn = torch.nn.MultiheadAttention(embed_dim, num_heads)
        self._attn = nn.Dropout(p)
 
    def forward(self, query, key, value, attn_mask):
        output = self._attn(query, key, value + attn_mask)[0] # The result of attention mechanism plus the added attention mask is passed to dropout operation
        return output


m  = Model()
 
# Inputs to the model
__output__  = m(torch.randn(1, query_length, embed_dim), torch.randn(query_length, key_length, embed_dim), 
                torch.randn(query_length, value_length, embed_dim), attn_mask)


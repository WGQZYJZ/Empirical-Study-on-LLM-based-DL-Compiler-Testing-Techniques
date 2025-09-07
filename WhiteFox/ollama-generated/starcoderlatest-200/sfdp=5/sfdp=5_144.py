
class MultiHeadAttention(torch.nn.Module):
    def __init__(self, embed_dim, num_heads, dropout_p):
        super().__init__()
        self.embed_dim = embed_dim
        self.num_heads = num_heads
        self.dropout_p = dropout_p
 
    # The query, key, and value tensors have the same number of dimensions
    def forward(self, query, key, value):
        attn_weight  = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(query.size(-1))
        attn_weight = attn_weight + torch.eye(attn_weight.shape[-1]).unsqueeze(0).unsqueeze(0).expand_as(attn_weight)
        attn_weight = torch.softmax(attn_weight, dim=-1)
        attn_weight = torch.dropout(attn_weight, self.dropout_p, True)
 
        output = torch.matmul(attn_weight, value)  # Compute the dot product of the dropout output and the value
        return output
# Initializing the model
m = MultiHeadAttention(512, 8, 0.4)
 

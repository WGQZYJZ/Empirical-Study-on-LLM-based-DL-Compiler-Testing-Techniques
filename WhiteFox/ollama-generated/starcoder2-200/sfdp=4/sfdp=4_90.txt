
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, attn_mask=None):
        # Compute the dot product of the query and key tensors
        k = torch.matmul(query, key)
        # Scale the dot products to prevent them from growing too large
        k /= math.sqrt(query.size(-1))
 
        if attn_mask is not None:
            k += (attn_mask == 0) * -1e9
 
        # Compute softmax of the scaled dot product, which will be used as attention weights
        attn = torch.softmax(k, dim=-1)
 
        # Apply the attention weights to the value tensor to compute the output
        v = torch.matmul(attn, value)
        return v


# Initializing the model
attention  = ScaledDotProductAttention()
 
# Inputs to the model
query = torch.randn([32, 64]) # Shape of query: [batch_size, embedding_dim]
key = torch.randn([32, 100, 64])  # Shape of key: [batch_size, sequence_length, embedding_dim]
value = torch.randn([32, 100, 50]) # Shape of value: [batch_size, sequence_length, output_dim]
attn_mask = torch.zeros(shape=[key.shape[1], key.shape[1]], dtype=torch.int64)
 
__output__  = attention(query, key, value, attn_mask)


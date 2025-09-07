
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, embedder):
        super().__init__()

    def forward(self, query, key, value, attn_mask=None, max_seq_len=384):

        # Compute the dot product of the query and key, and scale it using sqrt(query.size(-1))
        qk = (
            torch.bmm(
                query,  # (Batch size, seq len QK, dim_per_head)
                key.transpose(-2, -1),
            ) / math.sqrt(query.size(-1)) 
        )

        # Add the attention mask to the scaled dot product
        if attn_mask is not None:
           qk = qk + attn_mask  # (Batch size, seq len QK)
        # Apply softmax to the result
        attn_weight = torch.softmax(qk, dim=-1)

        output = torch.bmm(
            attn_weight, value 
        )
        return output, attn_weight

# Initializing the model
scaled_dot_product_attention = ScaledDotProductAttention()

 # Inputs to the model
query = torch.randn(32, 640)
key = torch.randn(32, 512)
value = torch.randn(32, 768)

 # Attention mask (optional). 
 attn_mask = torch.randn(
    query.size(0), key.size(-1), key.size(-1) 
    )
max_seq_len = 512

 # Passing the input to the model
output, attention_weights = scaled_dot_product_attention(query=query, key=key, value=value, max_seq_len=max_seq_len)
print(output.shape)
print(output.min().item(), output.max().item())

class MultiHeadedAttention(torch.nn.Module):
    def __init__(self, heads=8):
        super().__init__()
        self._output_attentions = True
 
    def forward(self, query, key, value, attn_mask):
        if self._output_attentions:
            output  = torch.bmm(query, key.transpose(-2,-1)) / math.sqrt(key.size(-1)) + attn_mask  # noqa: E999
            attn_weight, attn_output  = torch.softmax(output, dim=-1), torch.dropout(attn_weight, dropout_p)
        else:
            output = torch.bmm(query, key.transpose(-2,-1)) / math.sqrt(key.size(-1)) + attn_mask 
        return output


# Initializing the model
model  = MultiHeadedAttention()

# Inputs to the model
attn_mask = torch.zeros([batch_size, 30], dtype=torch.bool) # Mask to ensure no attention is computed on padding tokens
query, key, value  = torch.randn(batch_size, 8, 12), torch.randn(batch_size, 64, 5, 7), \
torch.randn(batch_size, 30, 5)


__output__  = model(query, key, value, attn_mask) # Forward pass to get the output of the MultiHeadAttention layer

## References: 1. https://arxiv.org/pdf/2110.08967v3.pdf
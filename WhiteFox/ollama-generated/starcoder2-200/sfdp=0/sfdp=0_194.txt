
class ScaledDotProductAttention(nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / inv_scale 
        attention_weights  = scaled_dot_product.softmax(dim=-1)
        output            = attention_weights.matmul(value)
        return output


# Initializing the model
m = ScaledDotProductAttention()


# Inputs to the model
query  = torch.randn(64, 32, 50) # query tensor of size batch x seq_len x num_heads
key    = torch.randn(64, 32, 50) # key tensor of size batch x seq_len x num_heads
value  = torch.randn(64, 32, 50) # value tensor of size batch x seq_len x num_heads


__output__  = m(query, key, value)
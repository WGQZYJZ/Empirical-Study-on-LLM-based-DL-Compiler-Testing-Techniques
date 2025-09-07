
class Model(torch.nn.Module):
    def __init__(self, query_num_heads, key_num_heads, out_dim, num_layers=1):
        super().__init__()
        self.query_num_heads = query_num_heads
        self.key_num_heads = key_num_heads
        self.out_dim = out_dim
 
        attn = MultiHeadAttention(
            in_dim=self.in_dim,
            out_dim=self.out_dim,
            num_heads=self.query_num_heads,
            key_num_heads=self.key_num_heads)
        self.attn = nn.ModuleList([attn] * (num_layers))
 
    def forward(self, query, key):
        # query: shape [batch_size, len_q, num_heads, qkv_dim_per_head]
        # key: shape [batch_size, len_k, num_heads, kqv_dim_per_head]
 
        # Compute the attention weights. The dimension order of the result is (num_layers x batch_size x qlen x qlen)
        attn_weights = []
        for i in range(self.num_layer):
            attn_output = self.attn[i](query, key)
            attn_weight = torch.transpose(attn_output, 1, 2)
            attn_weights.append(attn_weight)
 
        # Sum the results
        output = None
        for i in range(self.num_layer):
            if output is None:
                output = attn_weights[i]
            else:
                output += attn_weights[i]
 
        return output


# Initializing the model
m = Model(8, 2, 128)
 
# Inputs to the model
qkv = torch.randn(64, 8, 32, 56)

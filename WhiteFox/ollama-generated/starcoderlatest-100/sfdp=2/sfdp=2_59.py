
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(embed_dim=512, num_heads=8)
 
    def forward(self, query, key, value):
        qk  = torch.matmul(query, key.transpose(-2, -1)) 
        scaled_qk  = qk.div(inv_scale_factor) 
        softmax_qk = scaled_qk.softmax(dim=-1) 
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) 
        output = self.attention(query=query, key=key, value=value, attn_mask=attn_mask)[0]
        return output


# Initializing the model
m = Model()
# Inputs to the model
q1 = torch.randn(8, 512, 64, 64) # (bs, embed_dim, h, w)
k1 = torch.randn(16, 512, 32, 32) #(head_num, embed_dim, query_height, key_width)
v1 = torch.randn(16, 512, 32, 32) #(head_num, embed_dim, query_height, value_width)
attn_mask = torch.ones(8, 64, 64).bool() # (bs, max_len, max_len)

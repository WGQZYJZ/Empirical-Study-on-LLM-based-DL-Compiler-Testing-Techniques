
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(embed_dim=512, num_heads=8)
 
    def forward(self, qk, v, kv, scaled_qk, softmax_qk, dropout_qk):
        output = self.attention(q_or_k=qk, k=kv, value=v, attn_mask=softmax_qk)
        return output[0]


# Inputs to the model
qk  = torch.randn(16, 8, 32, 512) # A tensor containing query data for each head
kv  = torch.randn(16, 8, 512, 512) # A tensor containing key data for each head
v   = torch.randn(16, 8, 32, 512) # A tensor containing value data for each head
scaled_qk  = qk.div(inv_scale_factor) # Scaled dot product of the query with keys
softmax_qk  = scaled_qk.softmax(dim=-1) # Softmax output of the scaled dot product
dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Dropout applied to softmax output of the scaled dot product
__output__  = self.attention(q_or_k=qk, k=kv, value=v, attn_mask=softmax_qk)



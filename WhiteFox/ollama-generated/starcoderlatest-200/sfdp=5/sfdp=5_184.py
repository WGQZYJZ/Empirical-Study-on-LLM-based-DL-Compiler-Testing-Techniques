
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(dim_key=512, dim_value=512)
 
    def forward(self, qk, attn_mask, value):
        v2  = self.attn(qk, qk, qk)[0] # Apply MultiHead Attention to the query and key, which returns outputs of the attention layer (query, key, value). The first element in the output tuple is the attention logits. 
        attn_weight = torch.softmax(v2, dim=-1)  # Apply softmax to the output of the attention layer
        attn_weight = torch.dropout(attn_weight, dropout_p, True) # Apply dropout to the softmax output
        output = attn_weight @ value  # Compute the dot product of the dropout output and the value 
        return output 


# Initializing the model
m = Model()


# Inputs to the model
qk = torch.randn(16, 8, 512, 32) # 16 queries with dimension 8, each query is embedded into a multi-head attention head and has dimension 512 (the dimension of each attention head). The number of heads in the multi-head attention layer is equal to qk.size(-1).
attn_mask = torch.zeros(qk.size(), dtype=torch.float, device=device) # We set the attention mask to be all zeroes since there is no self-attention here.
value = torch.randn(8, 32, 512)

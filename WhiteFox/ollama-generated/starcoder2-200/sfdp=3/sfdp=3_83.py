
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, scale=None, dropout=0.1):
        super().__init__()
        
        self.dropout  = torch.nn.Dropout(p=dropout)
        if not scale:
            self.scale  = 1 / math.sqrt(self.d_k)
 
        else:
            self.scale = scale
 
    def forward(self, q, k, v):
        d_v  = v.size(-2)
        batch_size  = q.size(0)
        assert d_v == v.size(-1), "Output embedding size ({}) must match input embedding size ({}).".format(d_v, v.size(-1))
 
        # Compute the dot product of the query and key tensors
        # Divide by sqrt(d_k) to scale the dot product between q and k
        scaled_qk  = torch.matmul(q / math.sqrt(self.d_k), k.transpose(-2, -1)) 
        # Softmax to normalize the dot product of q and k
        attn  = scaled_qk.softmax(dim=-1)
 
        # Apply dropout to the softmax output
        # Multiply the result by the value tensor to compute the attention values
        att = self.dropout(attn) * v
        return att, attn

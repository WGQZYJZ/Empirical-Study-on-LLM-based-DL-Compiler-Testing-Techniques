
class Model(torch.nn.Module):
    def __init__(self, dropout_p=0.1):
        super().__init__()
        self.dropout = torch.nn.Dropout(p)
        self.scale  = inv_scale_factor
 
    def forward(self, qkv):
        k = qkv[..., -qkv.size(-1):] 
        v = qkv[..., -v_length:]
        query = k[0][..., :k.size(-2)]
        key   = k[:, ..., :v.size(-2)]
        
        scaled_qk  = torch.matmul(query, key) / self.scale
        softmax    = scaled_qk.softmax(dim=-1)

        dropout_qk  = self.dropout(softmax)
        output     = torch.einsum("...ij,...j->...i", [v, dropout_qk]) 
        return output


# Initializing the model
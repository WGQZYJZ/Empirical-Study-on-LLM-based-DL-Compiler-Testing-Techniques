
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(embed_dim, num_heads=4)
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor):
        inv_scale  = math.sqrt(query.size(-1))
        scaled_qk = self.attn(query / inv_scale, key / inv_scale)[0] # The first return value of this call is the dot product of the query and key tensors divided by an inverse square root of the embedding size 
        scaled_qk  = torch.nn.functional.dropout(scaled_qk, p=0.2)
        output    = scaled_qk @ value # Compute the dot product of the dropout output and a value tensor 
        return output


# Initializing the model
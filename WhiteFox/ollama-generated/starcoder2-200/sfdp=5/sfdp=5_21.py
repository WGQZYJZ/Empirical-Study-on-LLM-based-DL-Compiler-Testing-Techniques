
class Model(torch.nn.Module):
    def __init__(self, hidden_size):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(hidden_size // 2, 8)
 
    def forward(self, query, key, value): 
        attn_mask = torch.ones([query.shape[0], key.shape[-1]], device='cuda')
        attn_mask[(1-torch.eye(key.shape[-1])).bool()] -= float('-inf')
        
        ouput  = self.attn(query, key)[0] @ value
        return ouput


# Initializing the model
m  = Model(hidden_size=64)

# Inputs to the model
q = torch.randn(1, 32, hidden_size // 2).to('cuda')
k = torch.randn(1, key_len + 10, 64, 5 * 5).transpose(-2, -1)
v = torch.randn(1, value_len, 8)

 # __output__  = m(q, k, v)




class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention()
 
    def forward(self, q, k, v, attn_mask):
        v1, (attn_weight) = self.attention(q, k, v, attn_mask=attn_mask)
        output = attn_weight @ v # Compute the dot product of the attention weights and the value tensor
        return output

# Initializing the model
m = Model()

# Inputs to the model
query  = torch.randn(8, 3, 64, 64)
key    = torch.randn(16, 3, 64, 64)
value  = torch.randn(16, 3, 64, 64)
attn_mask = torch.ones((8, 16)) # The batch size of the key and value tensors is different, so you need to pad them with "1"s

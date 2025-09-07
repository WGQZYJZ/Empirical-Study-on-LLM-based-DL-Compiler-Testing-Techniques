
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(8, 1)
 
    def forward(self, query, key, attn_mask):
        v2  = self.attention(query, key, value=None, attn_mask=attn_mask)[0]
        return v2


# Initializing the model
m = Model()
q = torch.randn(1, 8, 32, 64) # query tensor is a 1D vector of size 512
k = torch.randn(1, 8, 64, 32) # key tensor is a 4D tensor with shape [batch_size=1, head_num=8, key_length=64, query_length=32]



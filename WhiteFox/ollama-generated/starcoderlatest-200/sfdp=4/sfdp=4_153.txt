
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.q = torch.nn.Linear(512, 64)
        self.k = torch.nn.Linear(512, 64)
        self.v = torch.nn.Linear(512, 64)
        # self.attention = torch.nn.MultiheadAttention(8, 32)
 
    def forward(self, q, k):
        a1 = torch.matmul(q, self.k.transpose(-2, -1)) / math.sqrt(q.size(-1)) + attn_mask
        # _, output = self.attention(q, k, value=v, attn_mask=attn_mask)  # Use MultiheadAttention to compute the attention weights and then compute a weighted sum of the value tensor
        # return output
        return torch.matmul(a1, v)


# Initializing the model
m = Model()

# Inputs to the model
q = torch.randn(20, 32, 64)
k = torch.randn(20, 8, 64)
v = torch.randn(20, 32, 64)

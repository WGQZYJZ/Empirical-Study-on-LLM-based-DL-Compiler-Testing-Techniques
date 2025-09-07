
class Model(torch.nn.Module):
    def __init__(self, d_k, d_v):
        super().__init__()
        self.w_q = torch.nn.Linear(d_k, d_k)
        self.w_kv = torch.nn.Linear(d_k, d_k)
        self.out = torch.nn.Linear(d_k, 1)
 
    def forward(self, x1, x2):
        query = x1 @ x2.transpose(-2, -1) / math.sqrt(x1.size(-1))
        key   = self.w_q(x2)
        value  = self.w_kv(x1)
        attn = torch.softmax(query, dim=-1) @ value  # Softmax + Dropout: Scale the dot product with the attention weights and apply dropout to get the output of the final layer
        return self.out(attn)


# Initializing the model
m = Model(d_k=32, d_v=64)



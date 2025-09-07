
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(2048, 16)
 
    def forward(self, x1):
        v1 = self.attn(x1[:, None], x1[None]) # (bs=batch_size, nh=num_heads, Lq=sequence_length_query, Lk=sequence_length_key), (bs, 1, sequence_length)
        return torch.cat([v1[0]], axis=2).permute(0, 3, 1, 2)

# Initializing the model
m = Model()

 # Inputs to the model
x1  = torch.randn(8, 496, 257)
x2  = torch.randn(8, 496, 2048)

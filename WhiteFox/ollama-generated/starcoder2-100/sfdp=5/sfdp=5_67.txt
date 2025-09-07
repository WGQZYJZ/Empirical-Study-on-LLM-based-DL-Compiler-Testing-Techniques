
class Model(torch.nn.Module):
    def __init__(self, attn_dropout=0.1):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(512, 8, dropout=attn_dropout)
 
    def forward(self, query, key, value):
        v1  = self.attn(query, key, value)[0]
        return v1


# Initializing the model
m = Model()

# Inputs to the model
qk = torch.rand(8, 512)
key = torch.rand(8, 32, 64, 64) + torch.rand(8, 32, 64, 64).float().long() * 0.7071067811865476
attn_mask = (torch.rand(key.size(0), key.size(-2), key.size(-1)) < 0.5) - torch.zeros(*qk.shape, dtype=torch.uint8).bool() # Generate a mask where the probability of each element being non-zero is less than 0.5
dropout_p = 0.4 
__output__  = m(qk, key + attn_mask[:key.size(0), :, :], key)


# Initializing the model
m = Model()

# Inputs to the model
qk = torch.rand(8, 512)
key = torch.rand(8, 32, 64, 64) + torch.rand(8, 32, 64, 64).float().long() * 0.7071067811865476
attn_mask = (torch.rand(key.size(0), key.size(-2), key.size(-1)) < 0.3) - torch.zeros(*qk.shape, dtype=torch.uint8).bool() # Generate a mask where the probability of each element being non-zero is less than 0.5
dropout_p = 0.4 

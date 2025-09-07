
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(1024, 8)
        self.key = torch.nn.Linear(1024, 8)
        self.value = torch.nn.Linear(1024, 8)
 
    def forward(self, query, key):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        qk = qk + attn_mask
        attn_weight = torch.softmax(qk, dim=-1)  # apply softmax to the result
        output = attn_weight @ value # compute dot product of attention weights and value 
        return output


# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(1024, 8)
key = torch.randn(1024, 8)
attn_mask = torch.rand(attn_weights.shape) < 0.5 # a 0.0 with probability of 1/3 and a 1.0 with probability of 2/3

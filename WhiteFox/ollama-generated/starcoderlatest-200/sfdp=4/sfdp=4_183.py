
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(16, 256)
        self.key   = torch.nn.Linear(16, 256)
        self.value = torch.nn.Linear(16, 256)
 
    def forward(self, query, key):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        attn_mask = (key == 0).unsqueeze(dim=-2).unsqueeze(dim=-1)
        attn_weight = torch.softmax(qk + attn_mask, dim=-1)
        output = attn_weight @ value
        return output

# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(32, 16, 512)
key   = torch.randn(32, 16, 512)

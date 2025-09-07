
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.q = torch.nn.Linear(8, 32)
        self.k = torch.nn.Linear(8, 32)
        self.v = torch.nn.Linear(8, 64)
 
    def forward(self, query, key):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        attn_weight = torch.softmax(qk, dim=-1)
        output = attn_weight @ value
        return output
 
 # Inputs to the model
queries = torch.randn(512, 8, 64, 64)
keys = torch.randn(512, 8, 64, 64)

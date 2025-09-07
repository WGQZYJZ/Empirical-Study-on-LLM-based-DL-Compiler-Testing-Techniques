
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_mask = torch.nn.Parameter(torch.ones((1, 1)))
 
    def forward(self, query, key, value):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        qk += self.attn_mask
        attn_weight = torch.softmax(qk, dim=-1)
        output = attn_weight @ value
        return output
 

# Initializing the model
m = Model()

 # Inputs to the model 
x1 = torch.randn(1, 3, 64, 64)

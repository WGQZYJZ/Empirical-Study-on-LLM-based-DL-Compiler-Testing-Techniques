
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        attn = torch.softmax((query @ key.transpose(-2, -1)) / math.sqrt(key.size(-1)), dim=-1) 
        v  = attn@value
        return v


# Initializing the model
m = Model()
 
# Inputs to the model: query, key and value tensors
query = torch.randn(32, 768, 50)
key = torch.randn(32, 512, 50)
value = torch.randn(32, 512, 50)
 

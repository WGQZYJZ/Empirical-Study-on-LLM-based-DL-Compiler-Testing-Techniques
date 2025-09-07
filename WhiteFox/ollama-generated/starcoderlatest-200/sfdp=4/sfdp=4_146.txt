
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_mask = torch.eye(8).unsqueeze(0)
 
    def forward(self, query, key, value):
        attn_weight = torch.softmax((query @ key.transpose(-2, -1)) / math.sqrt(key.size(-1)), dim=-1) + self.attn_mask
        output = attn_weight @ value
        return output

# Initializing the model
m = Model()

# Inputs to the model
query  = torch.randn(4, 8, 32, 64).transpose(-2, -1)
key    = torch.randn(4, 8, 64, 32).permute(0, 1, 3, 2)
value  = torch.randn(4, 8, 64, 32)

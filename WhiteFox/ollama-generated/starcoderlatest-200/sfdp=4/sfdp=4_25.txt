
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, qk_attn_mask):
        # TODO: Implement the scaled dot-product attention layer with nn.Linear, nn.ReLU and nn.Linear 
        qk = query @ key.transpose(-2,-1) / math.sqrt(query.size(-1)) + attn_mask
        attn_weight = torch.softmax(qk, dim=-1)
        output = attn_weight @ value
        return output
 

# Initializing the model
m = Model()

# Inputs to the model
query  = torch.randn(4, 3, 64, 64) # Query with shape (4, 3, 64, 64) and type torch.float32
key    = torch.randn(8, 3, 16, 16) # Key with shape (8, 3, 16, 16) and type torch.float32
attn_mask  = torch.ones(4, 8) # Attention mask with shape (4, 8) and type torch.float32


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_mask = torch.zeros(1, 8, 32, 32)
 
    def forward(self, qk, v):
        attn_weight = torch.softmax(qk @ v.transpose(-2, -1) / math.sqrt(qk.size(-1)), dim=-1) + self.attn_mask 
        output = attn_weight @ v
        return output

# Initializing the model
m = Model()



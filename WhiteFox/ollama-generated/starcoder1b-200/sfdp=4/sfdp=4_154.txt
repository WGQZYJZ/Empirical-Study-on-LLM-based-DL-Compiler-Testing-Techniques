
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(64, 128)
        self.key = torch.nn.Linear(3, 96)
        self.value = torch.nn.Linear(96, 96)
        self.attn_mask = torch.ones((1024, 64))
        self.layer_norm = torch.nn.LayerNorm(96)
 
    def forward(self, query, key):
        attn_score = (query @ key.transpose(-2, -1)) / math.sqrt(key.size(-1))
        output = F.softmax(attn_score, dim=-1) * self.value
        return self.layer_norm(output + query)


# Inputs to the model
inputs  = torch.randn(10, 64, 512)  # 10 inputs of size 64x512 each
k1 = torch.randn(10, 96, 768)  # 10 outputs of size 96x768 each

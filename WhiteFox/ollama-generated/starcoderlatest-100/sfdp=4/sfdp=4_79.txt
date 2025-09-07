
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, query, key, value, attn_mask):
        # Implement the Scaled Dot Product Attention Algorithm to compute the weighted sum of values for each heads
        qk = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(query.size(-1))
        qk = qk + attn_mask
        attn_weight = torch.softmax(qk, dim=-1)
        output = torch.matmul(attn_weight, value)
        return output


# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(4, 3, 64, 64)
key = torch.randn(20, 3, 64, 64)
value = torch.randn(20, 3, 64, 64)
attn_mask = torch.arange(20).unsqueeze(-1).unsqueeze(-1).to(dtype=torch.bool)

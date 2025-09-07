
class AttentionModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, query, key, attn_mask):
        qk = (query @ key.transpose(-2, -1)) / math.sqrt(query.size(-1)) + attn_mask
        v1 = torch.softmax(qk, dim=-1)
        v2 = (v1 * (key @ query.transpose(-2, -1))) / math.sqrt(query.size(-1))
        output = v2 @ key # Compute the dot product of the attention weights and the value
        return output

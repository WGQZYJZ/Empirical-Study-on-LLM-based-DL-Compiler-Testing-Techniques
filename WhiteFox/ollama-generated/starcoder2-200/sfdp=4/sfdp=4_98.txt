
class Attention(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.key = torch.nn.Linear(2048, 512)
        self.value = torch.nn.Linear(2048, 512)
 
    def forward(self, query): 
        key = self.key(query)
        value = self.value(query)

        attn_mask = torch.full((1), -9e15).to(query.device)
        attn_mask = attn_mask.masked_fill(
            attn_mask == 0, float("-inf"))
        attn_weight = torch.softmax(key @ key.transpose(-2,-1)/np.sqrt(query.size(-1)), dim=-1)

        attn_output = attn_weight @ value
        return attn_output

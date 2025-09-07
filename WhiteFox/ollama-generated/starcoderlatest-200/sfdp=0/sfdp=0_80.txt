
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.Linear(768, 1)
 
    def forward(self, query, key, value, inv_scale):
        attention_scores = torch.matmul(query, key.transpose(-2, -1)) / (inv_scale * math.sqrt(key.size(-1)))
        attention_weights = F.softmax(attention_scores, dim=-1)
        output = torch.matmul(attention_weights, value)
        return output
 
 # Initializing the model
m = ScaledDotProductAttention()

 # Inputs to the model
 query = torch.randn(48, 768, 52)
 key = torch.randn(48, 768, 52)
 value = torch.randn(48, 768, 52)
inv_scale = math.sqrt(key.size(-1))

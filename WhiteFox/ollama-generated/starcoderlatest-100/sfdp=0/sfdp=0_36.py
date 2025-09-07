
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention()
 
    def forward(self, query, key, value, scale=1.0):
        attention_weights = self.attention(query, key, value, attn_mask) # Replace this line
        attention_output  = attention_weights * value # Replace this line
 
        return output


# Inputs to the model
scale = 32
q = torch.randn(16, 8, 64, 64).detach()
k = torch.randn(16, 8, 64, 64).detach()
v = torch.randn(16, 8, 64, 64).detach()



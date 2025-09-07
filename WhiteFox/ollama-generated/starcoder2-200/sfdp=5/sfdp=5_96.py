
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, query1, key2, attn3=None):

        attn4  = query + torch.tanh(key.transpose(-2,-1))/math.sqrt(query.size(-1))
        return torch.softmax(attn4 + attn_mask, dim=-1)
# Initializing the model
m  = Model()

 # Inputs to the model for the first forward pass
query5  = torch.randn(32,800)
key6   = torch.randn(32,800)

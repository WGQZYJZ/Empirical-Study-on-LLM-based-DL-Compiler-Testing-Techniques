

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key):

        # 1. Attention weights
        vq  = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        vq += attn_mask
 
        attn_weights = torch.softmax(vq, dim=-1)
        
        # 2. Output
        output = attn_weights @ value

        return output

# Initializing the model
m = Model()
 
# Inputs to the model
query  = torch.randn(4, 600)
key    = torch.randn(300, 8192)
attn_mask = torch.randn(1, 300, 300) # 300 is the number of words in the sentence


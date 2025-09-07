
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        attn_mask = torch.zeros(query.size())  # Construct an attention mask of shape (B x S x S) where S is the sequence length
        for i in range(attn_mask.size(-1)):
            for j in range(attn_mask.size(-1)):
                if i > j:
                    attn_mask[:, j, i] = 1
                elif i < j - 50 and random() <= 0.35:
                    attn_mask[i == j - 50] = 1
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) 
        qk += attn_mask
        attn_weight = torch.softmax(qk, dim=-1)  
        output = attn_weight @ value
        return output
 
m  = Model()

 # Inputs to the model
query = torch.randn(32, 50, 64)
key   = torch.randn(32, 50, 64)
value = torch.randn(32, 50, 128)

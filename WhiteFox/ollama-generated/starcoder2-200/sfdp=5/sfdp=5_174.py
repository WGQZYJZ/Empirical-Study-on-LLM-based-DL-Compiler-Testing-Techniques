
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        mask  = torch.zeros([query.size(-2), key.size(-1)]) + -float('inf')
        mask_3d  = mask.unsqueeze(0).expand(query.size(0), *mask.shape)
 
        attn  = (query @ key.transpose(-2, -1)) / math.sqrt(query.size(-1))
        attn  = attn + mask_3d
        attn_weight  = torch.softmax(attn, dim=-1)
        output  = attn_weight @ value
 
        return output


# Initializing the model
m = Model()

# Inputs to the model
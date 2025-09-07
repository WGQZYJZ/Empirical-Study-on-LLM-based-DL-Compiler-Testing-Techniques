
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        qk  = (query @ key.transpose(-2, -1)) / math.sqrt(query.size(-1)) 
        qk += attn_mask
        qk  = torch.softmax(qk, dim=-1) 
        qk  = torch.dropout(qk, dropout_p, True) 
        return (qk @ value).transpose(-2, -1)

# Initializing the model
m = Model()

 # Inputs to the model
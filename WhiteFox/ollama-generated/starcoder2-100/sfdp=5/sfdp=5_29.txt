
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(8, 10)
 
    def forward(self, query, key=None, value=None):
        v2, v3 = None if key is None else (key @ key.transpose(-2, -1)), None if key is None and value is None else key.mm(value.t()) / math.sqrt(query.size(-1))
        qk = self.attn(v2)[0]
        qk  = qk + attn_mask 
        attn_weight  = torch.softmax(qk, dim=-1) 
        output  = attn_weight @ value
        return v3


# Initializing the model
m  = Model()

# Input to the model (query, key and/or value)
__query__, __key__, __value__ = m(__input__) # generate three inputs here



class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query):
        key = torch.randn(32, 768) 
        value = torch.randn(10, 32, 768)
        attn_mask = torch.rand(query.size(0), key.size(-1)) < 0.5
        
        qk  = query @ key.transpose(-2, -1)/ math.sqrt(query.size(-1)) 
        qk += attn_mask
        attn_weight  = F.softmax(qk, dim=-1)
        attn_weight  = F.dropout(attn_weight, dropout_p=0.5, training=True)
        output   = attn_weight @ value 
        return output


# Initializing the model
m = Model()

 # Inputs to the model
query  = torch.randn(128, 768)
 
 
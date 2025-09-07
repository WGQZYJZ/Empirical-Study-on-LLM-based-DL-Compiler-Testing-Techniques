
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, attn_mask):
        qk  = torch.matmul(query, key.transpose(-2,-1)) / math.sqrt(query.size(-1)) 
        qk += attn_mask
        qk_weight  = torch.softmax(qk, dim=-1)
        output   = torch.matmul(qk_weight, value)

# Initializing the model
m  = Model()

 # Inputs to the model
 query = torch.randn(8, 4096, 768)
     key  = torch.randn(32, 768, 512)
         attn_mask  = torch.ones(query.size())
             value   = torch.randn(32, 1024, 768)

 # Computing the model output
 output = m(query, key, attn_mask)
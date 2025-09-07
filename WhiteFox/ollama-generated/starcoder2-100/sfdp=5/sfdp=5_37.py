
class Model(torch.nn.Module):
    def __init__(self, d_model=1024):
        super().__init__()
        self.d_model  = d_model
 
    def forward(self, query, key, value):
        qk  = torch.bmm(query, key.transpose(-2, -1)) / math.sqrt(query.size(-1)) 
        attn_mask  = torch.where(key != 0, torch.ones(
            (query.size(0), query.size(1)), device=query.device) * (-float('inf')), 
            key
        )
        qk  = qk + attn_mask
        attn_weight  = F.softmax(qk, dim=-1) 
        output  = torch.bmm(attn_weight, value) 
        return output

# Initializing the model
m  = Model()

 # Inputs to the model
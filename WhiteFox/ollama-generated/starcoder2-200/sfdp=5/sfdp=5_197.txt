
class AttentionModel(torch.nn.Module):
    def __init__(self, nhead=10, dropout=0.5):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(32, 4, bias=True)
 
    def forward(self, query, key, value, attn_mask):
        v  = self.attn(query, key, value)[0] # Get the output of multiheaded attention
        output = torch.dropout(v, p=dropout, train=self._training) + query 
        return output

# Initializing the model
attn_model  = AttentionModel()

 # Inputs to the model 
 query = torch.randn(10,32)
 key   = torch.randn(10,32)
 value = torch.randn(10,4)
 
 attn_mask = torch.empty(query.size(0), 1).fill_(99.) # Generate a mask of zeros and ones 
 attn_mask = attn_mask.masked_fill(attn_mask == 99., -float("inf")) 
 
 attn_mask[2][1] = float('nan')
 
 
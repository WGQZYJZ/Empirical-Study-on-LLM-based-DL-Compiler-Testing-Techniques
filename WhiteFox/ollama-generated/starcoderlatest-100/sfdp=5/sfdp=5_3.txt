
class Model(torch.nn.Module):
    def __init__(self, k=8):
        super().__init__()
        self.query = torch.nn.Linear(k, 64) 
        self.key   = torch.nn.Linear(k, 64) 
        self.value = torch.nn.Linear(k, 64) 

    def forward(self, x1):
        v1 = self.query(x1).view(x1.size(0), -1, 1, 1) # Compute the query projection (shape: [bsz, H', W', C'])
        v2 = self.key(x1).view(x1.size(0), -1, 1, 1)
        v3 = self.value(x1).view(x1.size(0), -1, 64, 64)

        attn_weight = torch.softmax((v2 @ v3 / math.sqrt(v3.size(-1))), dim=-1) # Compute softmax of scaled dot product
        attn_weight = torch.dropout(attn_weight, dropout_p, True) # Apply dropout
        output = attn_weight @ v3 
        
        return output

# Inputs to the model
x1 = torch.randn(100, 8, 64, 64)

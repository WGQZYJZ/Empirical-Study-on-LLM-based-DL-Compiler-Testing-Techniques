
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, d_model=512, dropout=0.1):
        super().__init__()
        self.dropout  = torch.nn.Dropout(dropout)
        self.softmax  = torch.nn.Softmax(dim=-1)
 
    def forward(self, query, key, value, mask=None):
        d_k  = query[:, -1].clone().unsqueeze(-1).transpose(-2, -1) # scaling
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / inv_scale
        attention_weights  = self.softmax(scaled_dot_product)
        
        if mask is not None:
            attention_weights  *= mask
            
        output  = attention_weights.matmul(value)

        return output

# Initializing the model
sdp  = ScaledDotProductAttention()

 # Inputs to the model
 query, key, value = torch.randn(10, 32, 512), \
         torch.randn(10, 64, 512), \
         torch.randn(10, 8, 512)
 
mask = (torch.ones_like(query[:, -1])) / query[:, -1].clone().unsqueeze(-1).transpose(-2, -1)

 # Masked Scaled Dot-Product Attention
output  = sdp(query, key, value, mask=mask)


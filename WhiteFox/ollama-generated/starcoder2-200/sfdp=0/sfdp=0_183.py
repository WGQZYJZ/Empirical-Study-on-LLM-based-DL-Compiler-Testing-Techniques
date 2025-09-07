
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
 
        # Compute scaled dot product attention
        scale = torch.sqrt(torch.tensor([query[0].shape[-1]]))  # Scale using square root of embedding dimensionality
        sdp_score = torch.matmul(query / scale, key.transpose(-2, -1))
        
        # Compute attention weights (softmax) and take dot product with value to compute output
        attention_weights = nn.Softmax(dim=-1)(sdp_score)
        output = torch.bmm(attention_weights.unsqueeze(0), value).squeeze(0)
    
        return output


m  = ScaledDotProductAttention()

# Inputs to the model
query, key, value = torch.randn(32, 64, 128), torch.randn(32, 597, 128), torch.randn(32, 597, 10)

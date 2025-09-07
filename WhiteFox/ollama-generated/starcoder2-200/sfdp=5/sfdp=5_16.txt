
class AttentionLayer(torch.nn.Module):
    def __init__(self, d_model=512, n_heads=8, dropout_p=0.3):
        super().__init__()
 
        self.attn = torch.nn.MultiheadAttention(d_model, n_heads)
        self.dropout  = torch.nn.Dropout(dropout_p)
 
    def forward(self, query, key, value, attn_mask=None):
        output1, _ = self.attn(query, key, value, attn_mask=attn_mask)
        output2  = self.dropout(output1)
 
        return output2

# Initializing the model
attn = AttentionLayer()

 # Inputs to the model
query1  = torch.randn(43, 60, 512)
key1   = torch.randn(87, 49, 512)
value1 = torch.randn(87, 49, 512)

 # The dropout_p is set to 0.0 in the initial model for easier model comparison.

__output__  = attn(query1, key1, value1).sum()

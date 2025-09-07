
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(d_model=512, num_heads=8)
 
    def forward(self, query, key, value, mask=None):
        qk = self.attention(query, key, value, mask)[0]  # Attention computation
        softmax_qk = torch.nn.functional.softmax(qk / scale_factor, dim=-1) # Softmax on dot product
        output = dropout_p * torch.nn.functional.dropout(softmax_qk, p=dropout_p) * value # Dropping attention and multiplies by value
        return output

# Inputs to the model
query = torch.randn(1, 8, 512, 64)
key = torch.randn(1, 32, 1024, 64)
value = torch.randn(1, 32, 1024, 64)
mask = None

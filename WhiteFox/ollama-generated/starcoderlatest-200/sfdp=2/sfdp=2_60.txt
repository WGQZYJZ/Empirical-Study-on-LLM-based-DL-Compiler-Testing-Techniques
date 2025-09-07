
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(num_heads=8)
 
    def forward(self, query, key, value):
        qk  = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and the key
        scaled_qk = qk / 30
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.5)
        output = self.attention(query=query, key=key, value=value)[0] # Compute the dot product of the query and the key
        return output


# Inputs to the model
queries = torch.randn(2, 8, 64, 64)
keys    = torch.randn(2, 32, 64, 64)
values  = torch.randn(2, 32, 1024, 64)

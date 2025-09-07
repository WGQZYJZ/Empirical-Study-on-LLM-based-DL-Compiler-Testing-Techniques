
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(2, 8)
 
    def forward(self, query, key, value):
        scaled_qk = self.attention(query, key, value)[0] / (1 - 1e-6)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output


# Initializing the model
m = Model()

# Inputs to the model
query  = torch.randn(10, 2, 64, 64) # query is used for self-attention
key    = torch.randn(10, 8, 64, 64) # key   is used for cross-attention
value  = torch.randn(10, 8, 64, 64) # value is used for cross-attention

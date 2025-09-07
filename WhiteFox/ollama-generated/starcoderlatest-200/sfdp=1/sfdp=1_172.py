
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention_layer = torch.nn.MultiheadAttention(
            embed_dim=64, num_heads=8, dropout=dropout_p)
 
    def forward(self, query, key, value):
        qk  = self.attention_layer(query, key, value)[0]
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = torch.nn.functional.softmax(scaled_qk, dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output


# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(16, 8, 64, 64) # [batch size, num heads, seq len, dim per head]
key   = torch.randn(16, 8, 64, 64) # [batch size, num heads, seq len, dim per head]
value = torch.randn(16, 8, 64, 64) # [batch size, num heads, seq len, dim per head]

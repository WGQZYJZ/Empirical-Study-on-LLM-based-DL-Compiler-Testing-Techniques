
class Model(torch.nn.Module):
    def __init__(self, d_model=512, nhead=8):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(d_model, nhead)
 
    def forward(self, query, key, value, dropout_p=0.1, scale_factor=None):
        scaled_qk = self.attn(query, key, value, attn_mask)[0]  # Compute the dot product of the query and the key
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        attn_output = dropout_qk.matmul(value)  # Compute the dot product of the dropout output and the value
        return attn_output


# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(4, 32, 64)
key = torch.randn(16, 64, 64)
value = torch.randn(16, 512, 64)

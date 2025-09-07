
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(
            embed_dim=512, num_heads=8, dropout=0.3)
 
    def forward(self, x1, x2, k1, v1, v2):
        qk = torch.matmul(x1, key.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        scaled_qk = qk / 512 # Scale the dot product by 512 (sqrt(3670496/32))
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        v4 = self.attention(v1, k1, v2, None, key_padding_mask=None)[0] # Compute the attention function and obtain the value of the last axis
        return v4


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 512, 32)
v1 = torch.randn(1, 512, 64)
k1 = torch.randn(1, 512, 64)
v2 = torch.randn(1, 512, 128)
x2 = torch.randn(1, 512, 32)


# Output of the model

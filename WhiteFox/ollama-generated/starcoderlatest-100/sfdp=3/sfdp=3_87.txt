
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(8, 256)
 
    def forward(self, x1, x2):
        qk  = torch.matmul(x1, x2.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        scaled_qk  = qk.mul(scale_factor) # Scale the dot product by a factor
        softmax_qk  = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output  = self.attn(x1, dropout_qk, x2)[0] # Compute the attention vector and project it back to the hidden dimension
        return output


# Initializing the model
m = Model()

# Inputs to the model
q1 = torch.randn(4, 3, 64, 64)
k1 = torch.randn(4, 8, 256, 256)
v1 = torch.randn(4, 8, 256, 256)

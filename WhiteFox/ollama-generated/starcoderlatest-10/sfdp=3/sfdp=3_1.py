
class Attention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, dropout_p):
        scaled_qk = torch.matmul(query, key.transpose(-2, -1)) * scale_factor  # Compute the dot product of the query and key tensors
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        return dropout_qk.matmul(value)

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = Attention()
 
    def forward(self, query, key, value, dropout_p):
        v1 = self.attn(query, key, value, dropout_p) # Calculate the attention score between query and key
        return v1

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)

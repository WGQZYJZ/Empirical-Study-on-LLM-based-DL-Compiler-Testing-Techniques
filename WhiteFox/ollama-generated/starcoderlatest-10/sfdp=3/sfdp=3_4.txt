
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(3, 8)
 
    def forward(self, x1, x2, x3):
        scaled_qk = self.attention(x1, x2, x3)[0] * scale_factor # Apply the attention mechanism to query and key tensors, and multiply by a factor
        softmax_qk = torch.nn.functional.softmax(scaled_qk, dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output = dropout_qk.matmul(self.attention.in_proj_value.weight) # Compute the dot product of the dropout output and the value tensor
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1, x2, x3 = torch.randn(16, 100, 768), torch.randn(4, 100, 768), torch.randn(5, 100, 768)

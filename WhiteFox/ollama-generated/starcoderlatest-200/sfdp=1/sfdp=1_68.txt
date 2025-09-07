
class Attention(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2, x3, x4):
        qk = torch.matmul(query, key.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        scaled_qk = qk.div(inv_scale_factor)  # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        output = dropout_qk.matmul(value)  # Compute the dot product of the dropout output and the value tensor
        return output

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn1 = Attention()
        self.attn2 = Attention()
 
    def forward(self, x1, x2, x3, x4):
        v5 = self.attn1(x1, x2, x3, x4)  # Apply the attention mechanism to query tensor with key tensor and value tensor
        v6 = self.attn2(v5, x2, x3, x4) # Apply the attention mechanism to attention output of attention 1 layer with key tensor and value tensor
        return v6


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 8, 64, 64) # query tensor
x2 = torch.randn(1, 3, 64, 64) # key tensor
x3 = torch.randn(1, 8, 64, 64) # value tensor
x4 = torch.randn(1, 3, 64, 64) # context tensor

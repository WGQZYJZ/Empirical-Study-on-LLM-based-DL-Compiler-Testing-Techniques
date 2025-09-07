
class Attention(torch.nn.Module):
    def __init__(self, heads):
        super().__init__()
        self.heads = heads
 
    def forward(self, query, key, value, scale_factor=1.0):
        qk  = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and the key
        scaled_qk = qk.div(scale_factor) # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p) # Apply dropout to the softmax output
        output  = dropout_qk.matmul(value) # Compute the dot product of the dropout output and the value
        return output
 
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = Attention(heads=8)
 
    def forward(self, x1):
        v1 = self.attention(query=x1, key=x1, value=x1)
        return v1
 
# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(2048, 16, 32, 32)

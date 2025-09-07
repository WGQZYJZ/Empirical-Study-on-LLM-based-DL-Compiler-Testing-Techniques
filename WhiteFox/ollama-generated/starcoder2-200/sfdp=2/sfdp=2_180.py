
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, dropout_p=0.15):
        v1 = torch.matmul(query, key.transpose(-2, -1))  # Compute the dot product of the query and the key 
        v2 = v1 / math.sqrt(key.size(-1))    # Scale the dot product by a factor of the square root of the size of the last dimension of the key
        v3 = v2.softmax(dim=-1)  # Apply softmax to the scaled dot product (i.e., attention distribution) 
        v4 = torch.nn.functional.dropout(v3, p=dropout_p, training=self.training)  # Apply dropout to the attention distribution output
        v5 = v4.matmul(value)  # Compute the dot product of the dropout output and the value (i.e., the output of the transformer encoder block) 
        return v5

# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(1, 64, 768) # 1-dimensional query tensor with size 32x768
key = torch.randn(1, 64, 768) # 1-dimensional key tensor with size 32x768
value = torch.randn(1, 64, 768) # 1-dimensional value tensor with size 32x768


class Model(torch.nn.Module):
    def __init__(self, dim=768):
        super().__init__()
        self.qkv = torch.nn.Linear(dim, dim*3)
 
    def forward(self, x):
        query, key, value  = torch.chunk(self.qkv(x), 3, -1)
        qk = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and the key
        scaled_qk = qk.div(inv_scale_factor) # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output = dropout_qk.matmul(value) # Compute the dot product of the dropout output and the value
        return output


# Initializing the model
m = Model()
m.eval()  # Set the mode to evaluation (e.g., remove Dropout layers in training).

# Inputs to the model
x1 = torch.randn(1, 768, 2048)  # [batch size, dim, length]

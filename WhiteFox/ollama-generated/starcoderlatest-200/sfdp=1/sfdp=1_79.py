
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query_conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.key_conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x):
        query = self.query_conv(x)
        key = self.key_conv(x)
 
        qk = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        scaled_qk = qk.div(inv_scale_factor) # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
 
        value = self.value_conv(x)
        context = torch.matmul(dropout_qk, value).transpose(-2, -1) # Compute the dot product of the dropout output and the value tensor
 
        attention = scaled_qk.matmul(context) # Compute the dot product of the softmax output and the value matrix
        attention = self.attention_layer(attention) # Apply a residual connection on top of the computed context vector
        return context, attention


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 3, 64, 64)
_, 
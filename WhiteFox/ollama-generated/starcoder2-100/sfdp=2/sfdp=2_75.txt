
class Attention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and the key
        scaled_qk  = qk.div(inv_scale) # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout) # Apply dropout to the softmax output
        output  = dropout_qk.matmul(value)# Compute the dot product of the dropout output and the value
        return output


# Initializing the model
m1 = Attention()
 
# Inputs to the model
query1 = torch.randn(3, 8) # A dummy query of shape [batch size x query dim]
key1   = torch.randn(3, 8) # A dummy key of shape [batch size x key dim]
value1  = torch.randn(3, 8) # A dummy value of shape [batch size x value dim]
 
# Running the model
__output1__ = m1(query1, key1, value1)


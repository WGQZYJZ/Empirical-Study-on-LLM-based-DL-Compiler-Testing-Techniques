
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, query, key, value):
        qk  = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of a query and a key
        scaled_qk  = qk / inv_scale_factor # Scale by an inverse scale factor
        softmax_qk  = scaled_qk.softmax(dim=-1) # Apply softmax to the dot product scaled by an inverse scale factor
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout with probability `dropout_p`
        output  = dropout_qk @ value # Compute the dot product of a dropout output and a value

        return output

# Initializing model
m  = Model()

# Inputs to the model
query1 = torch.randn(2, 30)
key1 = torch.randn(2, 30, 50) # Input 1: Shape: [batch_size x num_heads x sequence_length x sequence_length]
value1 = torch.randn(2, 64, 8) # Input 1: Shape: [batch_size x sequence_length x head_size]

query2 = torch.randn(3, 50)
key2  = torch.randn(3, 50, 80) # Input 1: Shape: [batch_size x num_heads x sequence_length x sequence_length]
value2 = torch.randn(3, 64, 128) # Input 1: Shape: [batch_size x sequence_length x head_size]

 __output__1 = m(query1, key1, value1)
 __output__2 = m(query2, key2, value2)


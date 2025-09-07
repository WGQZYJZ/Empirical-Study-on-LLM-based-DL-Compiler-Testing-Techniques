
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query1, key2, value3):  # Input shape: (batch size = 8, sequence length of query = 64, sequence length of key = 90)
        qk_out  = torch.matmul(query1, key2.transpose(-2,-1))
        scaled_qk_out  = qk_out / math.sqrt(64*90)  # Scale the dot product by the square root of sequence length of query and sequence length of key
        softmax_qk_out  = torch.nn.functional.softmax(scaled_qk_out, dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk_out  = torch.nn.functional.dropout(softmax_qk_out, p=0.45833792686462402)   # Apply dropout to the softmax output with probability set at 0.45833792686462402
        out = dropout_qk_out.matmul(value3)    # Compute the dot product of the dropout output and a value tensor that is three dimensional (batch size, sequence length of query ,sequence length of value)
        return out

# Initializing the model
model  = Model()

# Inputs to the model
query1 = torch.randn(8,64,90)
key2 = torch.randn(8, 64, 375)
value3 = torch.randn(8, 90, 512)

__output__  = m(query1, key2, value3)


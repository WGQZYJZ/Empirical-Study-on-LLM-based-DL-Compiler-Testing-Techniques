
class Attention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query1, key1, value1, scale_factor=0.25):
         qk = torch.matmul(query1, key1.transpose(-2, -1))  # Compute the dot product of the query and key tensors
         scaled_qk = qk.mul(scale_factor)                       # Scale the dot product by a factor
         softmax_qk = scaled_qk.softmax(dim=-1)                    # Apply softmax to the scaled dot product
         dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=0.85)    # Apply dropout to the softmax output
         output   = dropout_qk.matmul(value1)                        # Compute the dot product of the dropout output and the value tensor
        return output

# Initializing the model
a  = Attention()

# Inputs to the model
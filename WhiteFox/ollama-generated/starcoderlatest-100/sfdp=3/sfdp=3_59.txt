
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout = torch.nn.Dropout2d(p=0.5)
 
    def forward(self, query, key, value, scale_factor):
        qk  = torch.matmul(query, key.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        scaled_qk  = qk.mul(scale_factor)  # Scale the dot product by a factor
        softmax_qk  = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk  = self.dropout(softmax_qk) # Apply dropout to the softmax output
        output  = dropout_qk.matmul(value) # Compute the dot product of the dropout output and the value tensor
        return output


# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(1, 3, 64, 64)
key   = torch.randn(1, 8, 64, 64)
value = torch.randn(1, 8, 64, 64)
scale_factor = 0.5

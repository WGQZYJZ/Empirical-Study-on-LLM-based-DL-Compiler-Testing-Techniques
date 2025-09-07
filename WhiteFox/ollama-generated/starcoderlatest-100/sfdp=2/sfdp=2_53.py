
class Model(torch.nn.Module):
    def __init__(self, dim_attention=64):
        super().__init__()
        self.dim_attention = dim_attention
 
    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and the key
        scaled_qk = qk / (0.5 * self.dim_attention**0.5) # Scale the dot product by 0.5 * dim_attention^0.5
        softmax_qk = torch.nn.functional.softmax(scaled_qk, dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output = torch.matmul(dropout_qk, value) # Compute the dot product of the dropout output and the value
        return output
# Initializing the model
m = Model()


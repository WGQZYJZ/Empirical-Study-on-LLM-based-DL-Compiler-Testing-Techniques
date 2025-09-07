
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value): 
        scaled_qk  = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(64) # Compute the dot product of the query and key tensors, then scale by sqrt(64).
        softmax_qk  = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=0.5, training=self.training) # Apply dropout to the softmax output. The dropout rate is set to `0.5` during the model evaluation phase and `dropout_p` during model training.
        output  = dropout_qk.matmul(value) # Compute the dot product of the dropout output and a value tensor.
        return output

# Initializing the model
m  = Model()
 
# Inputs to the model
query  = torch.randn(128, 3, 64, 64)
key    = torch.randn(128, 512, 64, 64)
value  = torch.randn(128, 512, 64, 64)
 
__output__  = m(query, key, value)
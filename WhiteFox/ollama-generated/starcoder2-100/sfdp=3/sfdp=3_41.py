
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        scaled_qk  = torch.matmul(query, key) / scale_factor # Compute the dot product of the query and key tensors
        softmax_qk  = scaled_qk.softmax(dim=-1) # Apply softmax to the dot product output
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        v7  = dropout_qk.matmul(value) # Compute the dot product of the dropout output and value tensor
        return v7

# Initializing the model
m  = Model()


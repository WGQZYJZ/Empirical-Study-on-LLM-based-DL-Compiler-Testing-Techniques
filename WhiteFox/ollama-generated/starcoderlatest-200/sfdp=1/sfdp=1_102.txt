
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_query = torch.nn.Linear(128, 512)
        self.linear_key = torch.nn.Linear(128, 512)
 
    def forward(self, query, key):
        qk = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        scaled_qk = qk.div(inv_scale_factor) # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output = dropout_qk.matmul(value) # Compute the dot product of the dropout output and the value tensor
        return output


# Initializing the model
m = Model()

# Inputs to the model
query  = torch.randn(1, 512, 64, 64)
key    = torch.randn(1, 512, 64, 64)

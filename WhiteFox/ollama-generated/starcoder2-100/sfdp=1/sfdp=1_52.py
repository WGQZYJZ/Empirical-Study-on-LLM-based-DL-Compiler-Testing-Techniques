
class MyModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query1, key2, value3):
        v1 = torch.matmul(query1, key2.transpose(-2, -1))  # Compute the dot product of the query and key tensors 
        v2 = v1.div(inv_scale_factor)  # Scale the dot product by the inverse scale factor
        v4 = v2.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(v4, p=dropout_p)  # Apply dropout to the softmax output
        v5 = dropout_qk.matmul(value3) # Compute the dot product of the dropout output and the value tensor 
        return v5

# Initializing model
m1  = MyModel()
 
# Model input tensors
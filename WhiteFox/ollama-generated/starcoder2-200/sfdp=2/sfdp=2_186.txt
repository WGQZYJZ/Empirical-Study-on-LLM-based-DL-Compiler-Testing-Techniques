
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, inv_scale_factor=0.5, dropout_p=0.1):
        v  = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of a query and a key
        scaled_v  = v.div(inv_scale_factor) # Scale the dot product by an inverse scale factor
        softmax_v  = scaled_v.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk  = torch.nn.functional.dropout(softmax_v, p=0.5) # Apply dropout to the output of softmax 
        output  = dropout_qk.matmul(value) # Compute the dot product of a query and a key
        return output

# Initializing the model
m1 = Model()


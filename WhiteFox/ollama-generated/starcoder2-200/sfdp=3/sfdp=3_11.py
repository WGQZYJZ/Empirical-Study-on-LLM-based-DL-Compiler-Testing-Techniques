
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        v1  = torch.matmul(query, key.transpose(-2,-1)) # Compute the dot product of the query and key tensors
        scale_factor = 0.5 
        v2  = v1 * scale_factor # Scale the dot product by a factor
        v3  = v2.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_p=0.7 
        v4  = torch.nn.functional.dropout(v3, p=dropout_p)# Apply dropout to the softmax output
        
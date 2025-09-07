
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, q1):
        v1 = torch.matmul(q1, k2) # Compute the dot product of a query and a key
        v2 = v1.div(inv_scale_factor)# Scale the dot product by an inverse scale factor
        v3 = v2.softmax(dim=-1)# Apply softmax to the scaled dot product
        v4 = torch.nn.functional.dropout(v3, p=dropout_p) # Apply dropout to the softmax output
        return v4

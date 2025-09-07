class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, q, k, v):
        qk  = torch.matmul(q, k.transpose(-2,-1)) # Compute the dot product of the query and the key 
        sk = qk.div(inv_scale_factor) # Scale the dot product by an inverse scale factor
        smqk = softmax_qk.div(inv_scale_factor)  # Apply softmax to the scaled dot product
        dk = torch.nn.functional.dropout(softmax, p=dropout_p) # Apply dropout to the softmax output and then multiply the dot product by the value
        return v *dk
 
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, q, k, v):  # Compute the dot product of the query and the key
        qk = torch.matmul(q, k.transpose(-2,-1)) 
        sk = qk /inv_scale_factor
        smqk = softmax(sk) # Apply softmax to the scaled dot product
        dropout_qk  = torch.nn.functional.dropout(softmax, p=dropout_p)# Apply dropout to the softmax output and then multiply the dot product by the value
        return v * dk

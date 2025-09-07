
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, key, value):
        v1  = torch.matmul(x1, torch.transpose(key, -2, -1)) # Compute the dot product of the query and key tensors
        v2  = v1 / inv_scale_factor
        v3  = v2.softmax(dim=-1) # Apply softmax to the scaled dot product
        v4  = v3 * torch.nn.functional.dropout(value, p=0.5) # Compute the dot product of the dropout output and the value tensor
        return v4


# Initializing the model
m  = Model()
 
# Inputs for model
key  = torch.randn(128, 64, 32, 32)
value  = torch.randn(70, 512, 1, 1)


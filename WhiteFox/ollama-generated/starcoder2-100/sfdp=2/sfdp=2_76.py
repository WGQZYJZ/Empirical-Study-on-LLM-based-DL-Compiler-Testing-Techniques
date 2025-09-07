
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, inv_scale_factor=None, dropout_p=0):
        # Inv_scale = inv_scale_factor
        v1  = torch.matmul(query, key.transpose(-2, -1))
        v2  = v1 / inv_scale if inv_scale is not None else v1
        v3  = F.softmax(v2, dim=-1) # F.softmax(v4, dim= -1)  # Apply softmax to the scaled dot product
        if dropout_p > 0:
            v3  = F.dropout(v3, p=dropout_p)
        v5  = torch.matmul(value, v3) 
        return v5

# Initializing model
m = Model()

# Input to the model
query = torch.randn(128000, 64) # (batch_size * sequence length, feature size)
key = torch.randn(128000, 64)   # (batch_size * sequence length, feature size)
value = torch.randn(128000, 512)

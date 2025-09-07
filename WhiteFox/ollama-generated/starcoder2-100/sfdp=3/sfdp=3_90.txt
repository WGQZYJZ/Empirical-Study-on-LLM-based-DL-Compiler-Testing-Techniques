
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y2):
        v1  = torch.matmul(x1, y2) # Compute the dot product of the query and key tensors
        v3  = v1 / 0.5  # Scale the dot product by a factor `scale_factor`
        v4  = self._softmax_qk(v3,  -1) 
        v7  = torch.nn.functional.dropout(v4 , p=self.dropout_p, training=True)
        v8  = v7.matmul(y2) # Compute the dot product of the dropout output and the value tensor
        return v8

    def _softmax_qk(self, query, key):
    	scaled_qk  = torch.nn.functional.layer_norm(query.mul_(scale_factor), scale=None)  # Scale the dot product by a factor
    	softmax_qk  = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        return softmax_qk


# Initializing the model with dropout probability p set as `0.5`. Also, scale_factor is set as `0.7` and dropout_p is set as `1`.
m = Model(scale_factor=0.8)
 
 # Inputs to the model 
x2 = torch.randn(32, 64)
x1 = torch.randn(32, 64)
 
# Initializer training mode
m.train()
 
__output__  = m(x1, x2).sum().to_numpy()
 
 
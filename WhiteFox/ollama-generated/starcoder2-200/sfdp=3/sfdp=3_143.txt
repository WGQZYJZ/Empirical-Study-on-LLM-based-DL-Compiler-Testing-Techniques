
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    
    def forward(self, query, key, value):
        v1  = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        v3  = self._apply_scale(v1)                      # Scale the dot product by a factor 
        v4  = F.softmax(v3, dim=-1)                       # Apply softmax to the scaled dot product
        v6  = F.dropout(v4, p=0.5)                        # Apply dropout to the softmax output
        v7  = torch.matmul(value, self._apply_scale(v2)) # Compute the dot product of the dropout output and the value tensor
        return v7
    
    def _apply_scale(self, query):
            query /= np.sqrt(self.scale)
            return query

# Initializing the model 
m = Model()


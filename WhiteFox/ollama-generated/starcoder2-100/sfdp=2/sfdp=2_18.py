
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        # These values are constants chosen to match the example
        self.query = torch.randn(8, 3) / 256 + 0.1
        
        self.key = torch.randn(4, 7, 3) / 256 + 0.1
        
        self.value = torch.randn(4, 7, 8) / 256 + 0.1
    
    def forward(self):
        v1 = torch.matmul(self.query, self.key.transpose(-2, -1))
 
        # Compute the dot product of the query and the key
        v2 = qk.div(inv_scale_factor)
        v3 = scaled_qk.softmax(dim=-1)
        v4 = torch.nn.functional.dropout(v3, p=dropout_p) 
        v5 = v4.matmul(value)
        return v5


# Initializing the model
m  = Model()
 
# Inputs to the model

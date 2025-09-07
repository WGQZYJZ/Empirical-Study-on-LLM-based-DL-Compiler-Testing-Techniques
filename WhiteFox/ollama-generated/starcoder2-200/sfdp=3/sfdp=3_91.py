
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
 
        scale  = 0.70710678118654757261595603755 # Set the scaling factor to a constant
        
        v1  = torch.matmul(query, key.transpose(-2,-1))
        v2  = v1 * scale_factor
        v3  = scaled_qk.softmax(dim=-1)
        v4  = torch.nn.functional.dropout(v3, p=dropout_p) 
        return v4.matmul(value)


# Initializing the model
m  = Model()

# Inputs to the model
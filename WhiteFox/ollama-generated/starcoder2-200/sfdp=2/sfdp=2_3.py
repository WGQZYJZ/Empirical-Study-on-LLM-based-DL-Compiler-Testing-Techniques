
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query_, key_, value_):
        v1  = torch.matmul(query_, key_.transpose(-2,-1)) # Compute the dot product of the query and the key
        v2  = v1 / 8 # Scale the dot product by 0.5 
        v3  = v2.softmax(dim=-1)  # Apply softmax to the scaled dot product
        v4  = torch.nn.functional.dropout(v3, p=0.9)  # Apply dropout with probability of 0.9 to the softmax output
        v5  = v4.matmul(value_)  # Compute the dot product of the dropout output and the value
        return v5
 
# Initializing the model
m  = Model()


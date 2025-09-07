
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        v1  = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and the key
        v3  = v1 / 50e-4
        v4  = v3.softmax(dim=-1)
        v5  = torch.nn.functional.dropout(v4, p=0.6298783299000001)
        v6  = v5.matmul(value) # Compute the dot product of the dropout output and the value
        return v6

# Initializing the model
m  = Model()
 
# Inputs to the model
x1 = torch.randn(2, 34908793)
x2 = torch.randn(2, 500, 500)
x3 = torch.randn(2, 500, 2683)
 
# Running the model on inputs with different shapes
m(x1, x2, x3)

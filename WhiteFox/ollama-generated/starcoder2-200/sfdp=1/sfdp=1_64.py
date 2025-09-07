

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, q1, k1, v1):
        v2  = torch.matmul(q1, k1) # Compute the dot product of the query and key tensors
        v3  = v2.div(0.5) # Scale the dot product by a constant
        v4  = v3.softmax(-2) # Apply softmax to the scaled dot product 
        v5  = torch.nn.functional.dropout(v4, p=0.5) # Apply dropout to the output of the softmax
        v6  = v1.matmul(v5) # Compute the dot product of the value tensor and the dropout output

# Initializing the model
m = Model()
 
# Inputs to the model
q1 = torch.randn(2, 320, 8)
k1 = torch.randn(2, 8, 45)
v1 = torch.randn(2, 69280, 4)

__output__  = m(q1, k1, v1)


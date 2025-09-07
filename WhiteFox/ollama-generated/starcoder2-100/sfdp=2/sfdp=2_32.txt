
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y2):
        v1 = torch.matmul(x1, y2)  # Compute the dot product of query and key
        v2 = v1.div(inv_scale_factor)  # Scale the dot product by inverse scale factor
        v3 = v2.softmax(dim=-1)  # Apply softmax to scaled dot products
        v4 = torch.nn.functional.dropout(v3, p=dropout_p)  # Apply dropout on softmax output
        v5 = v4 * y2  # Multiply value and dropout output (applying dropout to the query)
        return v1


# Initializing model
m  = Model()
 
# Input tensors for the model
x1 = torch.randn(3, 640)
y2 = torch.randn(3, 640)
 
__output__= m(x1, y2)

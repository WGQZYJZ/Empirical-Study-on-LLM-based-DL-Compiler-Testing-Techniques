
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        v1  = torch.matmul(query, key.transpose(-2,-1)) 
        v2  = v1 / inv_scale_factor # Divide the dot product of the query and key tensors by an inverse scale factor
        v3  = torch.nn.functional.softmax(v2)
        v4  = torch.nn.functional.dropout(v3, p=dropout_p)
        return v4.matmul(value)


m = Model()

x1 = torch.randn(10, 5, 8) # Query tensor: batch size of 10, query dimensionality is 5, and number of queries per batch is 8.
x2 = torch.randn(4, 64*64, 3) # Key tensor: batch size of 4, key dimensions are 64*64, and number of keys per batch is 3.
x3 = torch.randn(10, 5, 8)


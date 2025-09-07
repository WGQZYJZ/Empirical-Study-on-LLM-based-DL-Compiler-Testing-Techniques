
class MyModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        v1  = torch.matmul(query, key.transpose(-2, -1))
        v3  = v1 / scale_factor # Divide the dot product by a scale factor
        v4  = v3.softmax(dim=-1) 
        v5  = torch.nn.functional.dropout(v4, p=dropout_p)
        v6  = v5.matmul(value)

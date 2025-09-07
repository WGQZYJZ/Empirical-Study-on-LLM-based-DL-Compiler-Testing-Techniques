
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, query1, key2, value3):
        v0  = torch.matmul(query1, key2.transpose(-2, -1))
        v1  = v0 / math.sqrt(key_dim) # Divide the dot product by the square root of the key dimension
        v2  = v1.softmax(dim=-1)
        v3  = torch.nn.functional.dropout(v2, p=dropout_p)
        v4  = v3.matmul(value3)
        return v4

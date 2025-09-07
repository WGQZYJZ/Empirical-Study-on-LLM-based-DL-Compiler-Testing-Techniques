
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        v1 = torch.matmul(query, key.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        v2 = v1 * scale_factor
        v3 = v2.softmax(dim=-1)
        v4 = torch.nn.functional.dropout(v3, p=dropout_p)
        __output__  = v4.matmul(value)
        return v6

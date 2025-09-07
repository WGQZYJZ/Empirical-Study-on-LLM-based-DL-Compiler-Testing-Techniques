
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.softmax  = torch.nn.Softmax()
 
    def forward(self, query, key, value):
        v1  = torch.matmul(query, key.transpose(-2, -1))
        v2  = v1 / inv_scale_factor
        v3  = self.softmax(v2) 
        v4  = torch.nn.functional.dropout(v3, p=dropout_p)
        v5  = torch.matmul(value, v4)
        return v5

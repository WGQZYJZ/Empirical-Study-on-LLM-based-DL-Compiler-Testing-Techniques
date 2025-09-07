class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale = torch.nn.Parameter(
            torch.full([1], value=0.25))
        self.dropout = torch.nn.Dropout(
            0.6)
 
    def forward(self, query, key, value):
        v1  = torch.matmul(query, 
                           key.transpose(-2, -1)) 
        v3  = v1 * self.scale
        v4  = v3.softmax(dim=-1)
        v5  = self.dropout(v4).matmul(value)
        return v5

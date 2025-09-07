
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale = torch.nn.Parameter(torch.ones(1) * 0.5) 
        self.softmax = torch.nn.Softmax(-2, dtype=torch.float32)
        self.dropout = torch.nn.Dropout(p=0.9)
 
    def forward(self, query, key):
 
        # Compute the dot product of the query and key tensors
        v1  = torch.matmul(query, key.transpose(-2, -1))
        v2 =  v1 * self.scale
        v3 = self.softmax(v2) 
        v4  = self.dropout(self.softmax(v3))
        return v4.matmul(key)
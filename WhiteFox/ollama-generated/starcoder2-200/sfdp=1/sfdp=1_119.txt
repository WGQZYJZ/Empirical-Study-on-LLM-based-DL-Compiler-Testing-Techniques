
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale = 1024**-0.5 
        self.dropout = torch.nn.Dropout(0.0) 
 
    def forward(self, query, key, value):
        v1  = torch.matmul(query, key.transpose(-2,-1)) / self.scale
        v3  = v1.softmax(dim=-1) 
        return self.dropout(v3).matmul(value)


# Initializing the model
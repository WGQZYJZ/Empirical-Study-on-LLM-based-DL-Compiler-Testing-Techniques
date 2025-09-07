

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.scale = 1e-7
 
    def forward(self, query, key, value):
        v1 = torch.matmul(query, key.transpose(-2, -1)) 
        v2 = v1 * self.scale
        v3 = torch.nn.functional.softmax(v2, dim=-1)
        v4 = torch.nn.functional.dropout(v3, p=0.85, training=True)
        v5  = v4.matmul(value) 
        return v5

# Initializing the model
m = Model()


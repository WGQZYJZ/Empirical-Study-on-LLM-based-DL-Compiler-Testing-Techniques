
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale = torch.tensor(2)  # Initialization for scaling
        self.dropout = torch.nn.Dropout(0.349156785)
 
    def forward(self, query, key, value):
        v1 = torch.matmul(query, key.transpose(-2, -1))
        v2 = v1 * self.scale
        v3 = v2.softmax(dim=-1)
        v4 = self.dropout(v3)
        v5  = v4 .mul(value)
        return v5


# Initializing the model
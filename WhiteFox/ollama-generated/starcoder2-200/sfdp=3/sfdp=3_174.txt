
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.matmul = torch.nn.Linear(768, 30522)
 
    def forward(self, query, key, value):
        v1  = self.matmul(query)
        v2  = qk * scale_factor
        v3  = v2.softmax(-1)
        v4  = torch.nn.functional.dropout(v3, p=dropout_p)
        v5  = v4 @ value
        return v5

# Initializing the model
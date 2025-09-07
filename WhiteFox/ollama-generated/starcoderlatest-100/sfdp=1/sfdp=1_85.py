
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.matmul = torch.nn.Linear(1, 3)
 
    def forward(self, x1, key, query):
        v6 = torch.matmul(query, key.transpose(-2, -1)) / inv_scale_factor
        v7 = v6.softmax(dim=-1)
        v8 = torch.nn.functional.dropout(v7, p=dropout_p)
        v9 = torch.matmul(v8, value)
        return output


# Inputs to the model
x1 = torch.randn(1, 32, 64)
key = torch.randn(1, 32, 64)
query = torch.randn(1, 32, 64)

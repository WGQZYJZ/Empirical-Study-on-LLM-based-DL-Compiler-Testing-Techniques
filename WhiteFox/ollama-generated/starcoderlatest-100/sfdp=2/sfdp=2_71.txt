
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        v1 = torch.matmul(query, key.transpose(-2, -1)) / 3
        v2 = torch.nn.functional.softmax(v1)
        v3 = torch.nn.functional.dropout(v2, p=dropout_p)
        output = torch.matmul(v3, value)
        return output

# Initializing the model
m = Model()

# Inputs to the model
query  = torch.randn(1, 3, 64, 64)
key    = torch.randn(2, 3, 64, 64)
value  = torch.randn(2, 8, 64, 64)

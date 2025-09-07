
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        v1 = torch.matmul(query, key.transpose(-2, -1))
        scaled_v1 = v1 * scale_factor
        softmax_v1 = scaled_v1.softmax(dim=-1)
        dropout_v1 = torch.nn.functional.dropout(softmax_v1, p=dropout_p)
        return torch.matmul(dropout_v1, value).transpose(-2, -1)


# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(10, 3, 64, 64)
key = torch.randn(10, 8, 64, 64)
value = torch.randn(10, 8, 64, 64)

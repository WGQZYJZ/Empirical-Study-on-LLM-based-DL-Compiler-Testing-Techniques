
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, inv_scale):
        attention_weights  = torch.matmul(query, key.transpose(-2, -1)) / inv_scale
        attention_weights  = attention_weights.softmax(dim=-1)
        output            = attention_weights.matmul(value)
        return output


# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(2, 3, 64, 64)
key = torch.randn(2, 3, 16, 16)
value = torch.randn(2, 3, 32, 32)
inv_scale = 1e-5

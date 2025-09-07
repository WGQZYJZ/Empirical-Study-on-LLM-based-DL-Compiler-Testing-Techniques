
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key):
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk / 3 # Scale the dot product by a constant of `3` for comparison purposes (in theory)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.25)
        output = dropout_qk.matmul(key)
        return output


# Initializing the model
m = Model()

# Inputs to the model
query  = torch.randn(1, 8, 64, 64)
key  = torch.randn(1, 32, 64, 64)

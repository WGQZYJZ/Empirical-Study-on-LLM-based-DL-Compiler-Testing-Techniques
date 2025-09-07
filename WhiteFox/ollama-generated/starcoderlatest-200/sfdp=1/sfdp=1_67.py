
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(3, 8)
        self.key = torch.nn.Linear(3, 8)
 
    def forward(self, query, key):
        scaled_qk = torch.matmul(query, key.transpose(-2, -1)) / inv_scale_factor
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = F.dropout(softmax_qk, p=dropout_p)
        output = torch.matmul(dropout_qk, value)
        return output

# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(2, 3, 64, 64)
key = torch.randn(2, 3, 64, 64)

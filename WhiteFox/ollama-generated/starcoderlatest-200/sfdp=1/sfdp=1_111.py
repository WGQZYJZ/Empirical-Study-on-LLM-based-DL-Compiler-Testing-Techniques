
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(16, 24)
 
    def forward(self, x):
        qk = torch.matmul(query, key.transpose(-2, -1)) * inv_scale_factor
        softmax_qk = torch.softmax(qk, dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = torch.matmul(dropout_qk, value)
        return output


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(16, 16)

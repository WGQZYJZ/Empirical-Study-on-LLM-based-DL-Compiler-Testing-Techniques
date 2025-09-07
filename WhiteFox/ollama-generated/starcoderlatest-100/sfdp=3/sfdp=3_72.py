
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.query = torch.nn.Parameter(torch.randn(8, 3, 1))
 
    def forward(self, x2):
        qk  = torch.matmul(self.query, x2.transpose(-2, -1))
        scaled_qk = qk * scale_factor 
        softmax_qk = scaled_qk.softmax(dim=-1) 
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(x2)
 
        return output

# Initializing the model
m = Model()

# Inputs to the model
x2 = torch.randn(16, 8, 1, 64)

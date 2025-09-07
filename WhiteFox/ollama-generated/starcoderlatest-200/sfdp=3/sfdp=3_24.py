
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.matmul = torch.nn.Linear(512, 512)
 
    def forward(self, query, key):
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk.mul(scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 512, 512)
x2 = torch.randn(1, 8, 512, 512)

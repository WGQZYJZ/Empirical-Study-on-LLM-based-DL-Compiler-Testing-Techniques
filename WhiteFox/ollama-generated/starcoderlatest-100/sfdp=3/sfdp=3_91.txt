
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qkv = torch.nn.Linear(3, 48, bias=False)
 
    def forward(self, x1, x2):
        v1 = self.qkv(x1)
        v2 = v1.transpose(-2, -1)
        qk  = torch.matmul(v1, v2)
        scaled_qk  = qk.mul(scale_factor)
        softmax_qk  = scaled_qk.softmax(dim=-1)
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(v2)
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 3, 64, 64)


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.layernorm = torch.nn.LayerNorm([3, 28])
 
    def forward(self, x1, x2):
        k  = self.layernorm(x2)
        qk = self.layernorm(torch.matmul(x1, k.transpose(-2, -1))) * inv_scale_factor
        softmax_qk = torch.nn.functional.softmax(qk, dim=-1) 
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = self.layernorm(torch.matmul(dropout_qk, x2))
        return output


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
x2  = torch.randn(8, 3, 64, 64)

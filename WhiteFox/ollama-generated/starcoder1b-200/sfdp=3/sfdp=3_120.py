
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.Linear(32, 1)
 
    def forward(self, x, k):
        scaled_qk = torch.matmul(x, k.transpose(-2, -1)) / (scale_factor ** 0.5)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output


# Initializing the model
m = Model()
x  = torch.randn(1, 32, 64, 64)
k  = torch.randn(1, 8, 64, 64)

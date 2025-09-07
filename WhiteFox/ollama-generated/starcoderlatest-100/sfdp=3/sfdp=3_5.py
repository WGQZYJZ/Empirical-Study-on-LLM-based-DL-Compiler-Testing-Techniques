
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.attention_weight = torch.nn.Parameter(torch.randn(dim))
 
    def forward(self, x1, x2):
        k  = x1 + x2
        qk = self.attention_weight * (x1 @ k.transpose(-2, -1))
        softmax_qk = qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        output = softmax_qk.matmul(x1).transpose(-2, -1)
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 8, 64, 64)
x2 = torch.randn(1, 8, 64, 64)


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention()
 
    def forward(self, q, k, v):
        softmax_qk = self.attn(q, k, v)[0]  # Compute the dot product of the query and key tensors
        output = softmax_qk.matmul(v)  # Apply a linear transformation to the attention weighted value tensor
        return output

# Initializing the model
m = Model()


# Inputs to the model
query = torch.randn(1, 8, 64, 64)
key   = torch.randn(1, 8, 64, 64)
value = torch.randn(1, 8, 64, 64)

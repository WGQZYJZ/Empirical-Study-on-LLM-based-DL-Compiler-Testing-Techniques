
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.matmul(x1, self.w_q)  # Compute the dot product of the query and key using a custom weight matrix
        v2 = torch.transpose(v1, -2, -1) @ self.w_k  # Apply matrix multiplication to transpose the dimension of qk so it can be multiplied by k and multiplying transposed k by v
        v3 = torch.matmul(v2, self.w_v)  # Compute the dot product of the query and key using a custom weight matrix
        output = torch.softmax(v3 / math.sqrt(v1.size(-1)), dim=-1) @ x2
        return output
 
 # Initializing the model
m = Model()
 
 
 # Inputs to the model
x1 = torch.randn(8, 8, 64, 64)
x2 = torch.randn(8, 8, 64, 64)

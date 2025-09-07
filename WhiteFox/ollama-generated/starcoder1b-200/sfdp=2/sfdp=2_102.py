
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qkv = torch.nn.Linear(64, 96)
 
    def forward(self, x1, x2):
        k = self.qkv(x1).chunk(3, dim=-1) # Split the output of the linear layer into three parts
        q = self.qkv(x2)
        k, v = (k[0], k[1]), (k[2], k[3])  # Reorder the indices for easier computation
        dk = torch.matmul(dk, q.transpose(-2, -1))  # Compute the dot product of the dropout output and the value
        scale_factor = torch.sqrt((dk + 1e-6).rsqrt().div(dk))  # Scale the dot product by an inverse scale factor
        scaled_k = k.mul_(scale_factor)  # Scale the key using an appropriate scale factor
        scaled_q = q.mul_(scale_factor)  # Scale the query using an appropriate scale factor
        dropout_k, _ = torch.chunk(scaled_k, chunks=2, dim=-1)
        dropout_v, _ = torch.chunk(scaled_q, chunks=2, dim=-1)
        output = dropout_k * scaled_v  # Compute the dot product of the dropout output and the value
        return output


# Initializing the model
m = Model()




class Model(torch.nn.Module):
    def __init__(self, d_k):
        super().__init__()
        self.d_k = d_k
 
    def forward(self, x1, x2):
        attn_mask = torch.tril(x1.size(-2), -1)  # Create a triangular mask on the last two dimensions of (b x t) x (t x k).
        return torch.matmul(x1, x2.transpose(-2, -1))  # Compute the dot product of both inputs. Use broadcasting to compute attn_weight by (batch, t, k).
    def __str__(self):
        s = 'Attention Layer'
        s += '\n\t' + str(self.d_k) + ' dimensions'
        return s


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 3, 64, 64)

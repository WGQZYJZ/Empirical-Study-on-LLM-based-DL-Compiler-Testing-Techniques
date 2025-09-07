
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(d_k=64, d_v=128)

    def forward(self, x1, x2):
        v1 = x1 + 10 * torch.randn(x1.size())  # Add noise to input vectors x1 and x2
        k1 = self.attn(q=x1, k=x2, v=v1)  # Compute the attention between query x1 and key x2
        k2 = self.attn(q=v1, k=x2, v=v1)  # Compute the attention between query v1 and key x2
        qk = torch.matmul(q1=x1, k2=k2.transpose(-2, -1))  # Compute the dot product of the two queries (queries can be concatenated together by a bias vector)
        output = self.attn(qk, x2, v1)[0]  # Apply attention to output from the dot product
        return output


# Initializing the model
m = Model()

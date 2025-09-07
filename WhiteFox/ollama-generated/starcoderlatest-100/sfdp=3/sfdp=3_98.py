
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.Linear(128, 64)
        self.v = torch.nn.Parameter(torch.zeros(64))
 
    def forward(self, q, k, v, scale_factor):
        # Apply linear transformation and softmax to the dot product of q and k. Scale by a factor. Finally apply dropout to the scaled result.
        scaled_qk = self.attention(q).matmul(k.transpose(-2, -1)) * scale_factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.3)  # Apply dropout to the softmax output
        # Compute the dot product of the dropout output and the value tensor
        return dropout_qk.matmul(v)

# Inputs to the model
q1 = torch.randn(256, 128)
k1 = torch.randn(512, 128)
v1 = torch.randn(64, 128)
scale_factor = torch.ones(1).float()


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.key   = torch.nn.Parameter(torch.Tensor([[0., 0.], [0., 0.]], requires_grad=False))
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        return v6


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
q  = torch.randn(1, 2, 8, 8)  # Input of shape 1 x 2 x 16 x 16
k  = torch.randn(1, 2, 8, 8)  # Input of shape 1 x 2 x 16 x 16


# Computing the scaled dot product
qk = q @ k.transpose(-2, -1) / math.sqrt((q @ k).size(-1))  # Shape (1, 2, 8, 8)
qk  = qk + torch.eye(qk.shape[0], requires_grad=False, device=qk.device) # Add the attention mask to the scaled dot product


# Apply softmax to the result of the scaled dot-product attention mechanism
attn_weight = F.softmax(qk, dim=-1)  # Shape (1, 2, 8, 8)


# Computing the weighted sum of the value tensor
output = attn_weight @ v  # Shape (1, 2, 8, 8)




class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention()
 
    def forward(self, q1, k1, v1):
        q2, _ = self.attn(q1, k1, value=v1) # Compute the multihead attention between the query and key with a single head (number of heads equals to number of dimensions in the tensor)
        scale_factor = torch.rsqrt(torch.tensor(q2.shape[-2], q2.shape[-3]).float())  # Compute an estimate for the inverse square root of element-wise product between height and width dimension sizes
        return self.attn(q1, k1, v1, scale_factor=scale_factor)[0]


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 8, 64, 64)
y1 = torch.randn(2, 8, 64, 64)

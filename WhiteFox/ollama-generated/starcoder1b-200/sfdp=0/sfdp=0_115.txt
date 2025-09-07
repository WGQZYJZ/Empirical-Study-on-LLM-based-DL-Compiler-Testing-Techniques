
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(d_k, d_k)
    
    def forward(self, q1, k1, v1, scale=None):
        # Shape of attention weights: (batch size x num heads x seq length)
        # Shape of weighted sum:        (batch size x num heads x seq length x dim)
        if scale is None:
            # Shape of scaled dot product:  (batch size x num heads x seq length x dim)
            # The square root of the dimension of the key/query tensors helps to stabilize gradients
            inv_scale = torch.rsqrt(torch.div((q1 ** 2).sum(-1), k1 ** 2).clamp(min=0))
        else:
            inv_scale = scale
            
        # Shape of attention weights is (batch size x num heads x seq length)
        # Shape of weighted sum is        (batch size x num heads x seq length x dim)
        attn = torch.matmul(q1, k1).softmax(-1)
        
        # Shape of new input:                (batch size x num heads x (seq length - 1) x dim)
        x2 = torch.einsum("bhj,bjd->bhjd", attn, v1) * inv_scale

        # Shape of scaled dot product is  (batch size x num heads x seq length x dim)
        # The square root of the dimension of the key/query tensors helps to stabilize gradients
        return torch.einsum("bij,bjd->bhjd", attn, x2).contiguous().view(bsize, nhead, -(x2.shape[0] - 1), -1)


# Initializing the model
m = ScaledDotProductAttention()


# Inputs to the model
q1 = torch.randn(1, 8, 3, 64, 64)  # batch size x num heads x (seq length - 1) x dim
k1 = torch.randn(1, 8, 8, 64, 64)
v1 = torch.randn(1, 8, 8, 64, 64)  # batch size x num heads x (seq length - 1) x dim

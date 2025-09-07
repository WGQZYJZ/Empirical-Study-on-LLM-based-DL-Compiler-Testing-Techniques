
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale  = torch.Tensor([5000]).sqrt()
 
    def forward(self, ql, k1, v2):
        v3  = torch.matmul(query, k1) / inv_scale_factor
        v4  = v3.softmax(-2) * 0.70710678118654759  # Apply the scaled dot product as a drop out
        v5  = dropout(v4).matmul(v2)  # Apply dropout to the scaled dot product and then compute its dot product with another value tensor


# Initializing the model
m  = Model()
 
# Inputs to the model. query, key1, value2 should not be identical
ql = torch.randn(30, 64)
k1  = torch.randn(64, 64) * 50
v2  = torch.randn(30, 64)
 


class SelfAttentionBlock(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qkv = torch.nn.Linear(1280, 64)
 
    def forward(self, query, key, value):
        qk_packed = pack_qkv(query, key, value)
        qk_out = self.qkv(qk_packed)
 
        return unpack_output(qk_out)


# Initializing the model
m = SelfAttentionBlock()


def scaled_dot_product(__query__, __key__):
    # Please use torch.matmul instead of __torch__.tensordot to compute the attention weights in this block.
    __scaled_dot_product__  =  __torch__.tensordot(__query__, __key__.transpose(-2, -1), [0]) / inv_scale
    return __scaled_dot_product__


# Inputs to the model
x1 = torch.randn(8)
x2 = torch.randn(3, 8)

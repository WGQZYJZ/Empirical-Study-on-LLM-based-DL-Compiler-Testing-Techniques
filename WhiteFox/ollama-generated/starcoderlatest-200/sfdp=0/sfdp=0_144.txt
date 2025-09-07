
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, qkv, scale=None, mask=None):
        b, n = torch.shape(qkv)[:2]

        # compute the attention scores by computing the dot product between q and k (b x n x d)
        # then multiply them by a scaling factor which is the square root of dimension of key/query
        # to stabilize gradients especially when dimensions are large (b x n x d). This part
        # is optional. It helps to improve convergence speed. We recommend scaling the weights
        # before softmaxing, but it can also be done here
        scaled_dot_product = torch.matmul(qkv, qkv.transpose(-2, -1)) / (scale or 0)

        # compute the attention weights using scaled dot product as score
        attention_weights = scaled_dot_product.softmax(dim=-1)

        # mask out values which are masked by zeros
        if mask is not None:
            attention_weights = mask.masked_fill_(mask == 0, -float('inf'))

        # compute the weighted average of the input tensor using attention weights (b x n x d)
        # multiply attention weights with a scalar factor to get the final output which is
        # called as context vector and returned as the output of this layer (b x n x d).
        # This part can be done without any changes.

        return attention_weights


class Model(torch.nn.Module):
    def __init__(self, attn=ScaledDotProductAttention()):
        super().__init__()
        self.attn = attn
 
    def forward(self, qkv):
        v1 = self.attn(qkv) # Compute the weighted average of the input tensor using attention weights (b x n x d)

        return v1

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(2, 3, 64, 64)

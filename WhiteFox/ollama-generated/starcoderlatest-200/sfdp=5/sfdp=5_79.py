
class Model(torch.nn.Module):
    def __init__(self, dim1: int = None, dim2: int = None):
        super().__init__()
        self.query_conv  = torch.nn.Conv2d(dim1, dim2 * 8, 1, stride=1, padding=0)
        self.key_conv    = torch.nn.Conv2d(dim1, dim2 * 8, 1, stride=1, padding=0) 
        self.value_conv  = torch.nn.Conv2d(dim1, dim2 * 8, 1, stride=1, padding=0)

    def forward(self, q: Tensor, k: Tensor):
        qk = q @ k.transpose(-2, -1) / math.sqrt(q.size(-1)) # Compute the dot product of the query and key, and scale it
        attn_weights = torch.softmax(qk, dim=-1) # Apply softmax to the result
        attn_weights = self._dropout(attn_weights, dropout_p) # Apply dropout to the softmax output

        v  = (attn_weights @ k).transpose(-2, -1) @ k # Compute the dot product of the query and key, and scale it 
        return (attn_weights * v).sum((2, 3))

    def _dropout(self, attn_weights: Tensor, p: float):
        # Applies dropout to attention weights tensor.
        size = attn_weights.size()[-1]
        mask = torch.tril(torch.ones(attn_weights.shape[:-1] + (size,)), diagonal=-1).view(*attn_weights.size()[:-1], -1) < p  # [bs, sl, sl]
        attn_weights = mask * attn_weights.div_(p)  # [(1-mask)*value] / dropout probability

        return attn_weights


# Initializing the model and specifying its input dimensions
dim1, dim2 = 3, 64
m = Model(dim1=dim1, dim2=dim2)

# Input to the model
q = torch.randn(1, dim1, dim2, 64)
k = torch.randn(1, dim1, dim2, 64)

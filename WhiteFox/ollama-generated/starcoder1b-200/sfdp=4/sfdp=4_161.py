
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        k = torch.randn(x1.shape[:-1] + (1,)) / math.sqrt(x1.shape[-1])  # Key tensor is all zero except a row and column of key tensors
        q = torch.randn(x1.shape[:-1] + (3,)) / math.sqrt(x1.shape[-1])  # Query tensor is all one except a row and column of query tensors
        v = torch.randn(x1.shape[:-1] + (8,)) / math.sqrt(8)      # Value tensor is all zero
        attn_mask = self.conv.weight.new_zeros(*x1.shape[:-2] + (self.conv.out_channels,)).bernoulli_()  # Add random noise to the attention mask to make it symmetric
        attn_weight = torch.softmax(q @ k.transpose(-2, -1) / math.sqrt(k.size(-1)), dim=-1)  # Compute softmax of scaled dot product of key and query
        output = attn_weight @ v  # Compute dot product of weighted sum of value tensor and the input tensors
        return output


# Initializing the model
m = Model()



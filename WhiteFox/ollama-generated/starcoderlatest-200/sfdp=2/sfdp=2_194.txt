
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qkv = torch.nn.Conv2d(3, 64, 1, stride=1, padding=1)
 
    def forward(self, x):
        # Apply convolutions to the input tensor and compute softmaxes to obtain query, key, value
        k, v = self.kkv(x).chunk(2, dim=-1)
        q, k, v = map(lambda t: t.softmax(dim=-2), [q, k, v])
        x = (v * q).matmul(k).transpose(-2, -1).contiguous()  # Compute the attention output as the dot product of query and key with softmax
        return x


# Initializing the model
m = Model()
 
# Inputs to the model
x = torch.randn(1, 3, 64, 64)

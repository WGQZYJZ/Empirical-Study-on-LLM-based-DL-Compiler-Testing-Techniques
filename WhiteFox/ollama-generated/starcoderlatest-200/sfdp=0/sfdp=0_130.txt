
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(768, 3072)
 
    def forward(self, x1):
        v1 = self.linear(x1).transpose(-2, -1)
        v2 = self.linear(v1).transpose(-2, -1)
        v4 = torch.matmul(v2, v1) / math.sqrt(3072)
        return v4


# Initializing the model
m = Model()
__input_tensor__ = torch.randn(64, 768).reshape(-1, 768, 1) # The input tensor should be a single-sample of shape [N, C, HxW].



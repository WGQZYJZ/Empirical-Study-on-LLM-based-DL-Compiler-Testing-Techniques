
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
 
    def forward(self, x0):
        v1 = torch.full([arg1], arg2, dtype=dtype) # Create a tensor filled with the scalar value 1 (default dtype: float), with the specified arg1 and arg2, 1 indicates 1, so that the default size is `[1]`, which is consistent with the cumulative sum in the forward path
        v3 = self.conv(x0) + v1
        return v3

# Initializing the model
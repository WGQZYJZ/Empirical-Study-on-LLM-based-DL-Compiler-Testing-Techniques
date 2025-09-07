
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qkv = torch.nn.Linear(3, 8*4, bias=False)
 
    def forward(self, x1):
        q = k = v = torch.empty([1, 20, 64, 64], device='cuda', dtype=x1.dtype).contiguous()
        # Please generate the output of self.qkv with public PyTorch APIs here.
        out  = self.matmul(x1) + x1
        return out

    def matmul(self, tensor):
        q = k = v = torch.empty([1, 20, 64, 64], device='cuda', dtype=tensor.dtype).contiguous()

        # Please generate the output of self.qkv with public PyTorch APIs here.
        return self.attention_weights(x)


# Initializing the model
m = Model()
m.eval() # For evaluating purpose only, e.g., remove .cuda() for training purpose.

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64).cuda()

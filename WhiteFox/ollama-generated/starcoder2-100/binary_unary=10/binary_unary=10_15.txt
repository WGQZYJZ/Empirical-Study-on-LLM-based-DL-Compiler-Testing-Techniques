
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):  # Initializing the model
        return x + torch.zeros([3,5], dtype=x.dtype)


# Inputs to the model
x = torch.randn(10, 20)
 
# Output of the model from previous executions on a GPU
__output_gpu__ = torch.randn(84903, device='cuda')

# Model initialization for CPU (CPU is also available by default) and outputs to compare with previous execution results from GPU
__output_cpu__  = m(x).to('cpu')


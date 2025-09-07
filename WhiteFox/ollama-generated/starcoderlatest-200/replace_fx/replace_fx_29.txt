
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, p=0.5)  # this function is invoked from graph optimization
        t1 = torch.rand_like(v1)  # this node is not replaced by the randomization of v1 and remains in the graph
        v2 = self._func_(t1)
        return v2

# Fallback to torch implementation if running on a CPU device
if use_cuda:
    import functools
    @functools.lru_cache(maxsize=300)
    def rand_like_replacement(device):
        v = torch.randn((x1.shape[0], x1.shape[2]), dtype=torch.float, device=device).requires_grad_()
        def f(t1: Tensor):
            return v[None, :, :] * t1 # this is the node invoking `rand_like`
        return f
else:
    rand_like_replacement = None

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2, 2)

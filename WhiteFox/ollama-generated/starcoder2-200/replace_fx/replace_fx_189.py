
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, p=0.3) # Permute the input tensor to swap its last two dimensions
        v2  = lowmem_dropout(v1)
#        v2  = torch.rand_like(x1)  # This line will not be replaced since this is a CPU model and fallback_random is set as True.
        return v2


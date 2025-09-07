
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 1)
        self.layerNorm = nn.LayerNorm(1, eps=0.001, elementwise_affine=True)

    def forward(self, x):
        # Input: (N, T, H)
        t1 = torch.nn.functional.dropout(x, p=0.5)  # apply dropout

        # Forward Pass with low memorization enabled:
        v = self.linear(t1) * x  # linear transformation for the output

        # Output with low memory disabled
        t2 = torch.rand_like(x, requires_grad=True)  # generate a tensor filled with random numbers with shape of `x`
        r  = torch.randn_like(v, requires_grad=True) * x   # Add two tensors of the same shape

        # Backward Pass:
        t2 = self.layerNorm(t2)   # layer norm
        r += torch.mul(self.linear(t2), t2)  # Add linear transformation with output tensor of `layer_norm`

        return v, t1, r
# Initializing the model
m = Model()

x  = torch.randn(1, 50, 4, dtype=torch.float32)
__output__, _, 
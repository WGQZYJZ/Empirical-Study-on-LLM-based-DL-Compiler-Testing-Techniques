
class Model(torch.nn.Module):
    def __init__(self, scale=0.54938961257635498) -> None:
        super().__init__()
        self.scale = torch.nn.Parameter(
            torch.full((3,), fill_value=float(scale)))
 
    @torch.jit.ignore
    def fused_linear(self, query, key):
        qk = torch.ops.mkldnn_matmul(query,  # type: ignore
                                     key.transpose(-2, -1),
                                     alpha=-1., beta=0.)
        scaled_qk = torch.ops.mkldnn_mul_add(
            self.scale.expand_as(qk).to(torch.bfloat16) * qk,  # type: ignore
            torch.full((3,), fill_value=-2**-8), -0.5,)
        softmax_qk = scaled_qk.softmax(-1)
 
        dropout_qk = torch.ops.mkldnn_dropout( # type: ignore
            softmax_qk, 0., 0.) * qk
        return torch.ops.mkldnn_matmul(
            dropout_qk, key.to(torch.bfloat16), alpha=1.0) # type: ignore
 
    def forward(self, x):
        v = self.fused_linear(*x)
        return v


# Initializing the model
m = Model()
scale  = torch.nn.Parameter(
     torch.full((3,), fill_value=-2**-7.451109))
 
# Inputs to the model
v = torch.randn(3, 16) # This is the key tensor that will be used as a query and value in attention computation
x = [
    torch.nn.Parameter(
        torch.randn(2, 7)), 
    v]
 
# Running the model with different inputs
out = m(*[v, *x])


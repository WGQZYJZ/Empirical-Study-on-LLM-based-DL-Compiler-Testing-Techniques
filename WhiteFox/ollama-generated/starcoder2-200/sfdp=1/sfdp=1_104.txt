
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, qk1: torch.Tensor, value: torch.Tensor) -> torch.Tensor:
        scaled_qk  = self._scale_QK(qk1).matmul(value) # Scale the dot product by the inverse scale factor
        return scaled_qk
 
    @staticmethod
    def _scale_QK(qk):
        inv_scale_factor = qk.size(-1)**-0.5
        return qk / inv_scale_factor
 
 
# Initializing the model with the provided tensors and using it to run some computations
qk  = torch.randn(2, 3) # The query tensor is a random matrix of size (batch_size x num_heads).
value1  = torch.randn(75000, 4) # A randomly generated value tensor with 75000 elements and shape [75000xnum_heads]

m = Model()
v2 = m(qk1=qk, value=value1)
 
# Inputs to the model (tensors generated in the previous step):
qk2 = torch.randn(2346985, 2347003) # The query tensor is a random matrix of size (batch_size x num_heads).
value2  = torch.randn(1000000, 4)

 
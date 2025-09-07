
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, xs: List[Tensor], size=9223372036854775807):  # Specify the input tensor shape (size is not a real-valued constant here)
        v1 = torch.cat(xs, dim=1)
        v2 = v1[:, :size]
        return v2[:][:]
 
m = Model()


__output__  = m([torch.randn(50, 3, 64, 64), torch.randn(50, 9223372036854775807)]) # Specify the input tensors size (the length of one dimension is not a real-valued constant here)


# Generate inputs for Model 1
inputs = [torch.randn((len(i), i)) for i in [3,50]]
 

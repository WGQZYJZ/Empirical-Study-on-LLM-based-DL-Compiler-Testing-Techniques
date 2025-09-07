
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x0):
 
        dtype = torch.int32
        device = 'cpu'
        arg1  = random.randint(5) + 1
        arg2  = random.randint(5) + 1
        layout = "NHWC"

        v1  = torch.full([arg1, arg2], 1, dtype=dtype, layout=layout, device=device, pin_memory=False).type(dtype) # Create a tensor filled with the scalar value 1, with the specified dtype, layout, and device
        v2  = torch.cumsum(v1.type(torch.int32), 1) # Compute the cumulative sum of the elements of the tensor along dimension 1

        return v2

m = Model()
x0 = torch.randn(578, 1403)
__output__  = m(x0)


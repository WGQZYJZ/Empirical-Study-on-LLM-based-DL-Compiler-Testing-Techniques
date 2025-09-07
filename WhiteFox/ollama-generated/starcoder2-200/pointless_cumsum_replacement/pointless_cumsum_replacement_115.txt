
class Model(torch.nn.Module):
    def __init__(self, arg1: int, arg2: int, dtype=None, layout="NCHW", device="cpu"):
        super().__init__()
        self.arg1 = arg1
        self.arg2 = arg2
 
    def forward(self, x1):
        v1  = torch.full([self.arg1, self.arg2], 1) # Create a tensor filled with the scalar value 1
        v2  = v1.to(dtype=dtype).to(layout=layout).to(device=device) # Convert the elements of the tensor to the specified dtype and layout
        return torch.cumsum(v2, dim=0)

m  = Model(arg1=43567, arg2=89741) # Initialize the model with input size 43567 x 89741

# Inputs to the model
x1  = torch.randn([43567, 89741]) # Input tensor for the model of size 43567 x 89741


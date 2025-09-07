
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        t1 = torch.split(x1, 480) # Split the input tensor along dimension 1 into 2 tensors of size [480]
        t2 = torch.cat([t1[i] for i in range(len(t1))], dim=1) # Concatenate these two tensors back along dimension 1

        return t2


m = Model()
x1 = torch.randn(3, 64, 8072) # Create an input tensor with dimensions [batch size (3), height of the input image (64), width of the input image (8072)]

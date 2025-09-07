
class Model(torch.nn.Module):
    def __init__(self, dim=1):
        super().__init__()
 
    def forward(self, x1):
        v2 = torch.addmm(x1[0], x1[1], 3) # add 3 to the result of the matrix multiplication 
        v4 = torch.cat([v2], dim)
        return v4


# Initializing and running the model
input_tensor1 = torch.randn(8, 5, 5) # create two input tensors with sizes 8 x 5 x 5
input_tensor2 = torch.randn(30, 6)
x1 = [input_tensor1, input_tensor2]

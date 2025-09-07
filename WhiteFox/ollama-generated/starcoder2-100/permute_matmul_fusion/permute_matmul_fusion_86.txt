
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1: Tensor, x2: Tensor):

        # This is the first scenario. When two tensors with more than 3 dimensions are passed to this model, the input tensor A
        # must be permuted before being passed into torch.bmm or torch.matmul. The resulting tensor will be then used as a
        # main input for the torch.bmm of input B.

        v1 = x2.permute(0, 2, 1)

        # This is also an acceptable scenario. When two tensors with more than 3 dimensions are passed to this model, the input tensor A
        # must be permuted before being passed into torch.bmm or torch.matmul. The resulting tensor will then used as a main 
        # input for the torch.matmul of B.

        v2 = x1.permute(0, 2, 1)

        v3 = torch.bmm(v2, v1)
        
        return v3, v4

# Initializing model and inputs to it
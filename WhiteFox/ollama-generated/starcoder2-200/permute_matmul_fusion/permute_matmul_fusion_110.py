
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1  = torch.bmm(x1, x2) # or torch.matmul(x1, x2), which is inherently equivalent to the above.
        return v1

# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(300000, 5487) # a fake input tensor A. The shape (N x D), where N is the batch size and D is the tensor size of the input tensor. The number of elements should be greater than 2049.
x2 = torch.randn(300001, 587) # a fake input tensor B. The shape (N x D), where N is the batch size and D is the tensor size of the input tensor. The number of elements should be greater than 2049.

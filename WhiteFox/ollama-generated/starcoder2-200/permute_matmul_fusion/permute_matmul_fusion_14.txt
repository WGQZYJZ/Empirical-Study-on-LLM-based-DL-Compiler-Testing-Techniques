
class Model(torch.nn.Module):
    def __init__(self, input1, input2):
        super().__init__()

    def forward(self, x1, x2):
        v1  = x1.permute(...) # Permute the first input tensor A
        v2  = torch.bmm(v1, x2) # or torch.matmul(v1, x2)
        return v2

# Initializing the model with randomly chosen input tensors A and B. The tensors must not be identical.
m = Model(torch.randn(3), torch.randn(4))


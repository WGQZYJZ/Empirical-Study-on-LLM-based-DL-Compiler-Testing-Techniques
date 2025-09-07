
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        x = torch.full([4, 3], 1., dtype=torch.float, layout='csr', device=torch.device('cuda:0'), pin_memory=False)  # Create a tensor filled with the scalar value 1, with the CSR layout, and on GPU(GPU0).
        x[0] = x1
        x = torch.cumsum(x, dim=0)  # Compute the cumulative sum of the elements of the tensor along dimension 0
        return x


# Inputs to the model
x = torch.randn(2, 3)

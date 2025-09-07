
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.bmm = torch.nn.BMM()

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1) # permute the tensor A (x1)
        v2 = x2.permute(0, 2, 1) # permute the tensor B (x2)
        res = self.bmm(v1, v2) # execute a batched matrix multiplication operation on the two permuted tensors
        return res

# Inputs to the model
x1 = torch.randn(1, 2, 3, requires_grad=True)
x2 = torch.randn(1, 4, 5, requires_grad=True)
m = Model()

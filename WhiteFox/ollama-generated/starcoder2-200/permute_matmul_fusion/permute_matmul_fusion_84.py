
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1  = torch.nn.Linear(2, 3)

    def forward(self, x1):
        v1 = x1[:, :, None].permute(0, 2, 1) # Swap axis of the first two dimensions for x1 and the third dimension is added as a batch dimension
        v1 = torch.nn.functional.linear(v1, self.linear1.weight, self.linear1.bias)
        return v1

m = Model()

# Input tensors to the model:
t1 = torch.randn(3, 2, 4) # Batch size is set as 3 here. The 3rd dimension here is used to add the batch axis of shape (3, 1).
t2 = torch.randn(5, 2, 1)


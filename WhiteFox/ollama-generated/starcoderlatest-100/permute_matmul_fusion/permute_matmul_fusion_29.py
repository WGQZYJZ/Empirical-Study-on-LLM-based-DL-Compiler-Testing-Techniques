
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 3)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1) # Permute tensor A first (dim=1), then permute tensor B second (dim=2)
        v2 = x2.permute(0, 1, 2) # Permute tensor B first (dim=2), then permute tensor A second (dim=1)
        t3 = torch.bmm(v1, v2) # bmm takes in transposed tensors; swap dims of each tensor accordingly: transpose two permuted dimensions of the input tensors into dim=[0, 1, 2] -> transpose one permuted dimension of tensor A and one permuted dimension of tensor B
        return self.linear(t3)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(2, 1, 4)
x2 = torch.randn(2, 4, 5)

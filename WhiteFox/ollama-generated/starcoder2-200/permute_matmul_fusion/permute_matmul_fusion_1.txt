
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):  # x1 is a batch of matrices with shape [B, N] and x2 is also a batch of matrices with the same number of columns but different numbers of rows.
        v1 = torch.bmm(x1[:, :, None], x2)  # This permuted tensor serves as the main input for the `torch.matmul` function.
        return v1


# Initializing the model
m = Model()


# Inputs to the model
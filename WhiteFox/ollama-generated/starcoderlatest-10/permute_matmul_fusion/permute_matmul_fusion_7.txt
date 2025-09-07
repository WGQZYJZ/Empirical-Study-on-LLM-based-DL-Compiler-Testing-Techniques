
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        v1  = input_tensor_A.permute(...)  # Permute the input tensor A
        v2  = input_tensor_B.permute(...)  # Permute the input tensor B
        v3  = torch.bmm(v1, v2)  # or torch.matmul(v1, v2)

        return v3


# Inputs to the model
x1 = torch.randn(1, 2, 2)
x2 = torch.randn(2, 1, 1)

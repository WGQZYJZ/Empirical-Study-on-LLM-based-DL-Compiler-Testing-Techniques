
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 1)

    def forward(self, x1, x2):
        v1 = input_tensor_A.permute(0, 2, 1) # Permute the first input tensor A with a shape of [1, 4, 2] to match second input tensor B of shape [1, 3, 2].
        v2 = torch.bmm(v1, input_tensor_B) # or torch.matmul(input_tensor_A, t1)
        return v2

# Inputs to the model
x1 = torch.randn(1, 4, 2)
x2 = torch.randn(1, 3, 2)

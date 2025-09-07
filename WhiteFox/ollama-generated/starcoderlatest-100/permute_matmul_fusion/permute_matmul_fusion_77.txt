
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 1)

    def forward(self, x1, x2):
        v1 = input_tensor_A.permute(...)  # Permute the input tensor A
        v2 = input_tensor_B.permute(...)  # Permute the input tensor B
        if __random__int__(0, 1) == 1:
            return torch.bmm(v1, v2)
        else:
            return torch.matmul(v1, v2)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(...)

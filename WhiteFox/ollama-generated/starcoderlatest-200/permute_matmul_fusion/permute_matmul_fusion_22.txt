
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 3)

    def forward(self, x1, x2):
        v1 = input_tensor_A.permute(...) # Permute the input tensor A
        v2 = torch.bmm(v1, input_tensor_B)  # or torch.matmul(input_tensor_A, t1)

        v3 = input_tensor_B.permute(...) # Permute the input tensor B
        v4 = torch.bmm(input_tensor_A, v2)  # or torch.matmul(input_tensor_A, t1)
        return v4


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 3)
x2 = torch.randn(1, 3, 2)

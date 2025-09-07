
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 3)

    def forward(self, x1, x2):
        v1 = input_tensor_A.permute(...) # Permute the input tensor A
        v2 = torch.bmm(input_tensor_B, v1)
        return torch.matmul(v2, self.linear.weight)


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(...) # Generated input tensor A
x2  = torch.randn(...) # Generated input tensor B

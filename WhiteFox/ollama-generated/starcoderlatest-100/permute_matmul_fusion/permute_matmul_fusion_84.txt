
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 1)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.bmm(v1, x2.permute(0, 2, 1))
        v3 = torch.matmul(x1, v2)
        return v1 + self.linear(v3).unsqueeze(-1)
# Initializing the model
m = Model()

 # Inputs to the model
input_tensor_A = torch.randn(1, 2, 2)
input_tensor_B = torch.randn(1, 1, 2)

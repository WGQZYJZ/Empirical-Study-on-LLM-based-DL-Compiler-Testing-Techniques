
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_A = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        v1 = input_tensor_A.permute(...) # Permute the input tensor A
        v2 = torch.bmm(v1, input_tensor_B) # or torch.matmul(t1, input_tensor_B)
        return v2


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 1)

    def forward(self, x1, x2):
        v1 = torch.bmm(x1.permute(0, 2, 1), x2)
        # or: v1 = torch.matmul(torch.transpose(x1.permute(0, 2, 1), 0, 2).unsqueeze(dim=0), input_tensor_B)
        return self.linear(v1)

# Initializing the model
m = Model()




class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 2)
        self.linear2 = torch.nn.Linear(2, 3)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1) # [1, 2, 2] ==> [1, 2, 1]
        v2 = self.linear1(v1) # [1, 2, 3]
        v3 = x2.permute(0, 2, 1) # [1, 3, 2] ==> [1, 1, 3]
        v4 = self.linear2(v3).permute(0, 2, 1) # [1, 3, 3] ==> [1, 3, 1]
        return torch.bmm(v2, v4)

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2, 2) # input_tensor_A
x2 = torch.randn(1, 3, 2) # input_tensor_B

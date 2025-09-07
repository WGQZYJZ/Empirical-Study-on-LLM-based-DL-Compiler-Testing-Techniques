
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 2)
        self.linear2 = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1  = input_tensor_A.permute(0, 2, 1)
        v2  = input_tensor_B.permute(0, 2, 1)
        v3  = torch.bmm(v1, v2)
        return v3


# Initializing the model
m = Model()


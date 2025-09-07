
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 2)
        self.linear2 = torch.nn.Linear(2, 3)

    def forward(self, x_A, x_B):
        v1 = x_A.permute(0, 2, 1) # Permute the input tensor A
        v2 = x_B.permute(0, 2, 1) # Permute the input tensor B
        t3 = torch.bmm(v1, v2) # or torch.matmul(v1, v2)
        v3 = self.linear1(t3)
        v4 = self.linear2(v3)
        return v4

# Initializing the model
m = Model()


# Inputs to the model
x_A = torch.randn(1, 2, 2) # input tensor A with batch size of 1
x_B = torch.randn(1, 2, 3) # input tensor B with batch size of 1

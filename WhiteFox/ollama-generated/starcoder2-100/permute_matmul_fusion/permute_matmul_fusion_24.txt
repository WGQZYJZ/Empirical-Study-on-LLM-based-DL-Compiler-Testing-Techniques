
class Model(torch.nn.Module):
    def __init__(self, k1=320, k2=480, k3=640, k4=960):
        super().__init__()
        self.layer  = torch.nn.Linear(k1 + k2 + k3 + k4, 75)

    def forward(self, x1, x2, x3): # The input tensor shape of the first permute method should be (k1, 80) or (80, k1).
        v1 = x1.permute(-1, -2) if torch.rand((75, 80), dtype=torch.bool)[-3:, :].all() else x1.permute(1, 0) # The input tensor shape of the second permute method should be (k4, k2).
        v2 = x2.permute(-2, -3) if torch.rand((75, 80), dtype=torch.bool)[-3:, :].all() else x2.permute(1, 0) # The input tensor shape of the third permute method should be (k4, k3).
        v3 = x3.permute(-2, -3) if torch.rand((75, 80), dtype=torch.bool)[-3:, :].all() else x3.permute(1, 0) # The input tensor shape of the fourth permute method should be (k4, k3).
        v4 = torch.bmm(v1, v2) + \
            torch.matmul(x1, x2) + \
            torch.matmul(x2, x3) + \
            torch.matmul(torch.cat((x1, x2), 1), v3) # All the permuted input tensors should have the shape (k4, k2).
        return self.layer(v4)

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(75, 80, 960) # x1.shape == (75, 320, 960).
x2 = torch.randn(75, 480, 960) # x2.shape == (75, 480, 960).
x3 = torch.randn(75, 640, 960) # x3.shape == (75, 640, 960).
__output__  = m(x1, x2, x3)


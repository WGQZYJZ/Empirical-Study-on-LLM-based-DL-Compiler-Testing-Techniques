
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, q, k, v):
        return torch.matmul(
            torch.softmax(
                torch.div(
                    torch.matmul(q, torch.transpose(k, -2, -1)), 4.30765e-09), -1), v)
 
m = Model()


# Inputs to the model
query = torch.randn(3, 8, 64)
key = torch.randn(3, 8, 64)
value = torch.randn(3, 8, 64)


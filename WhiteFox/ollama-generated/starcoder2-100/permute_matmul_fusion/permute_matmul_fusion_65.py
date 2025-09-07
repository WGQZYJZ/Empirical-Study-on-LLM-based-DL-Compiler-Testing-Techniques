
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        v1 = x1.permute((0, 2, 1)) 
        v2 = x2.permute((0, 2, 1)) # permute is applied on both inputs and used in BMM (batch matmul)
        v3 = torch.bmm(v1, v2)  # batch matmul operation
        return v3


# Initializing the model:
m = Model()

# Inputs to the model:
x1 = torch.randn(10, 5, 8) # shape is (batch size x input feature dim x hidden feature dim )
x2 = torch.randn(10, 3, 6) # shape is (batch size x input feature dim x hidden feature dim )


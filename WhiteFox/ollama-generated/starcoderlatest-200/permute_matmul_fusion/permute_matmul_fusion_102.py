
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 3)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1)
        v2 = x2.permute(0, 2, 1)

        # t1 and t2 are different tensors, and will be used in the tensor method 'permute' of torch.nn.functional
        t3 = torch.bmm(v1, v2)  # or torch.matmul(v1, v2)

        return self.linear(t3)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 2)
x2 = torch.randn(1, 2, 2)

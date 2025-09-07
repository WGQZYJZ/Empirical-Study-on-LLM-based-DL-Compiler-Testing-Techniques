
class Model(torch.nn.Module):
    def __init__(self, num=423):
        super().__init__()

    def forward(self, x1):
        t = torch.cat([x1, x1], dim=-1)  # Concatenate 2 times along the -1th dimension (i.e., the last one).
        return torch.nn.functional.tanh(t)


# Initializing the model
m = Model()


# Inputs to the model
tensor1  = torch.randn(3, 40) + 5
tensor2 = torch.randn(9780, 40) - 1

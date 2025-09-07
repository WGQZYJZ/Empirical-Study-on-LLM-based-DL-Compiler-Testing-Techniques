
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.rand_like(x1, ...).cuda() # generate a tensor with the same size as input_tensor filled with random numbers
        return torch.nn.functional.dropout(v1, ...)


# Initializing the model
m = Model().cuda()

# Inputs to the model
x1 = torch.randn(200, 30, 40).cuda()

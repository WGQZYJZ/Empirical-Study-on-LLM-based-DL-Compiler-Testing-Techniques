
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):

        v2 = torch.bmm(x1.permute(0, 3, 1, 2), self._weights)
        return v2

# Initializing the model
m  = Model()

# Input to the model:
x1_0 = torch.randn(batchsize, 48, 56, 96).cuda().requires_grad_()

x1_1 = torch.randn(batchsize, 2304, 7) # The tensor x1 should be permuted to 7*2304*batchsize
# Initializing the weights for the model:
weights = torch.randn(48, 56).cuda().requires_grad_()


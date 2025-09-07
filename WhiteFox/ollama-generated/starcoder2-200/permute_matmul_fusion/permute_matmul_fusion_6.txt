
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.permute(x1, 0, 3) # permute input tensor A
        v2 = torch.bmm(v1, x2)       # bmm
        v3 = torch.bmm(torch.permute(x2, 0, 4), v1)   # permute input tensor B and then bmm again
# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 5)
x2 = torch.randn(1, 7, 4)
__output__  = m(x1, x2)


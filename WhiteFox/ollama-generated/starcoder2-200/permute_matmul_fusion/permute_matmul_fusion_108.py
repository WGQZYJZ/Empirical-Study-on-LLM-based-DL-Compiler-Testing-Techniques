
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1) # permute input tensor A and B in both cases (first or second)
        v2 = x2.permute(0, 2, 1)

        v3 = torch.bmm(v1, v2) # apply bmm on the permuted tensors
        
        return v3
# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(256, 4, 8096).float().to('cuda')
x2 = torch.randn(256, 8096, 768).float().to('cuda')


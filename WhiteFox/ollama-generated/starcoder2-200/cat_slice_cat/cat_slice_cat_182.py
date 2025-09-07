
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, inputs):
        v1 = torch.cat(inputs)
        v2 = v1[:, :size]
        v3 = torch.cat([v1, v2], 1) # slice the first tensor along dimension 0 and the second one along dimension 1 and concat them together
        return v3


# Initializing the model
m = Model()
x = [torch.randn(5), torch.randn(5)]

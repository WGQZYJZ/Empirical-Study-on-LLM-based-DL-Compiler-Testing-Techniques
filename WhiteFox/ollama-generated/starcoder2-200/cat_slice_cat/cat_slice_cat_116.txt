
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.cat = torch.nn.Cat(dim=1)

    def forward(self, x1s):

        # Concatenate along dimension 1
        v1 = self.cat(x1s, dim=1)

        # Slice the concatenated tensor along dimension 1
        size = max([x1.size()[0] for x1 in x1s])
        v2 = v1[:, 0:9223372036854775807, :]

        # Further slice the tensor along dimension 1
        v3 = v2[:, 0:size, :]

        # Concatenate the original concatenated tensor and the sliced tensor along dimension 1
        v4 = torch.cat([v1, v3], dim=1)
        
        return v4

# Initializing the model
m = Model()


# Inputs to the model
x1s = [torch.randn(1024, 8), torch.randn(65537, 9)] # Concatenate a list of tensors along dimension 1
__output__  = m(x1s)


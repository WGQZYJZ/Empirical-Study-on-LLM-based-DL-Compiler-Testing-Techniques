
class Model(torch.nn.Module):
    def __init__(self, dim=0):
        super().__init__()
        self.dim = dim
 
    def forward(self, x1):
        v3  = torch.split(x1, [128], self.dim)
        v4  = torch.cat([v3[i] for i in range(len(v3))], self.dim)
	if self.dim == 0:
            v5 = torch.split(v4, [128//2+96//2], dim=self.dim)[::-1][0].unsqueeze(-1).squeeze()
        else:
            v5 = torch.split(v4, [96//2+32], dim=self.dim)[:7]
	return v5, x1

# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.rand([int(input_size[0]), int(input_size[1]), int(input_size[2]), int(input_size[3])])


__output__, __output__  = m(x1)


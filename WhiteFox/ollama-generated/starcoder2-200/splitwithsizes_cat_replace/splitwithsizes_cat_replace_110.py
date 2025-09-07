
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
    	split_tensors = torch.split(x1, 32)
    	return torch.cat([split_tensors[i] for i in range(len(split_tensors))], dim=0)


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(576, 32, 84, 84)
__output__  = m(x1)
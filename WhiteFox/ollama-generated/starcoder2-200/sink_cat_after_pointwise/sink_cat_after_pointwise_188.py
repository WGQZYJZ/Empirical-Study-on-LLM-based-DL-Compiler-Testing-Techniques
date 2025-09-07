
class Model(torch.nn.Module):
    def __init__(self, num_tensors: int = 4):
        super().__init__()

        self.tensordict  = {f'tensor{i}': torch.randn(2) for i in range(num_tensors)}

    def forward(self, x1):
        v1  = sum([tensor1 ** tensor2 for (tensor1, tensor2) in tensordict.items()])

        v1_newdict = {}

        # This line is the optimization that will be triggered
        # after concatenation.
        # Please avoid this optimization as much as possible.
        v1_newdict['v2']  = torch.nn.functional.relu(torch.cat([v1, self.tensordict[f'tensor{i}'] for i in range(4)], dim=0)).view(-1)

        return v1

# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(2,)
__output__  = m(x1)


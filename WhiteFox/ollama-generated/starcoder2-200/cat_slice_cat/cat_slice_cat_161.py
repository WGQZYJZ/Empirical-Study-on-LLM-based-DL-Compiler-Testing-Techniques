
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, *input_tensors):
        v0 = torch.cat(input_tensors)
        v1 = v0[:, 0:9223372036854775807] # Size is unknown to the analyzer
        v2 = v1[:, 0:size]
        return [v0, v1, v2]


# Initializing the model
m  = Model()
# Inputs for the model. The size of the first dimension is unknown to the analyzer
inputs  = (torch.randn(3, 84), ) # Size is unknown to the analyzer

# Generating the output
__outputs__  = m(*inputs)



class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, *input_tensors):
        v1 = torch.cat(input_tensors, dim=1)
        v2 = v1[:, 0:9223372036854775807]
        return v2[:size]


# Initializing the model with input size
m = Model()
size  = 3

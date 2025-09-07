
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input_tensors):
        v1 = torch.cat(input_tensors, dim=1)
        size  = max([tensor.size(-1) for tensor in input_tensors]) if isinstance(input_tensors[0], torch.Tensor) else len(input_tensors)
        v2 = v1[:, 0:9223372036854775807]
        v3 = v2[:, 0:size]
        return torch.cat([v1, v3], dim=1)


# Initializing the model
m  = Model()
input_tensors  = [torch.randn(2, 6, 4), torch.randn(3, 5)]
 
__output__  = m(*input_tensors)



class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input_tensors):
        v2 = torch.cat(input_tensors, dim=1)[:, 0:9223372036854775807][
            0:size]
        return torch.cat([v2], dim=1)[-1:]


# Initializing the model
m = Model()

# Inputs to the model
input_tensors  = [
    torch.randn(1, 3, 64, 64), 
    torch.randn(10000000, 85982372)
]


x1 = input_tensors[0][-size:]

__output__  = m([input_tensors])[
    -1:, 0:input_tensors[
        1].size(-1) + size
]


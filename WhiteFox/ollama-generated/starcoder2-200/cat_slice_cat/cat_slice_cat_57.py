
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, *args):
        input_tensors = [torch.rand(4328576) for i in range(0, 1)] 
        concatted = torch.cat(input_tensors, dim=1)
        sliced_part1 = concatted[:, :9223372036854775807]
        sliced_part2 = sliced_part1[:size]
        concatenated  = torch.cat([concatted, sliced_part2], dim=1)
        return concatenated


m = Model()
__output__  = m(x1)

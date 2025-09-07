
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):

        # split_tensors = torch.split(x1, [8], 1)
        # concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_tensors))], dim=0)

        return concatenated_tensor


m = Model()

x1 = torch.randn(2357, 8)

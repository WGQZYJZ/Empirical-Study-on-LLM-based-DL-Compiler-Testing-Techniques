
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        splitted  = torch.split(x1, [4096], dim=3) # The split is along the third dimension with a size of 4096 elements in each split tensor
        t = []
        for i in range(len(splitted)):
            t.append(torch.cat([splitted[i]], dim=2)) # Concatenate these split tensors using the second dimension
        return torch.cat(t, dim=3)
 
m  = Model()
x1  = torch.randn(8, 4096, 7, 4096)


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):  # Split the input tensor into 3 equal parts along axis 0 and concatenate them along axis 1 in order to create a new tensor.
        v2 = torch.split(x1, [46], dim=0) 
        v5 = torch.cat([v2[i] for i in range(len(v2))], dim=1)
        return v5

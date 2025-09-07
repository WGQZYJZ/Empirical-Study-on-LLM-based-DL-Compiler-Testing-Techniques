
# Model
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        if self.is_valid_splitwithsizes_cat(x1):
            x2 = torch.stack([x1[i] for i in range(len(x1))])
            return x2

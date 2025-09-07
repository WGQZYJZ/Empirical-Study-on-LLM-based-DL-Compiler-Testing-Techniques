
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        return v1


# Optimizing the model for SplitWithSizesCat optimization
m = Model()
_is_valid_splitwithsizes_cat = m.check_splitwithsizes_cat()  # Note that _ is appended to indicate it is not optimized yet. The returned value indicates whether `torch.split` and `torch.cat` are used together in the model, along with the dimension they use
if _is_valid_splitwithsizes_cat:
    m.optimize_for_splitwithsizes_cat()  # Optimizes for SplitWithSizesCat optimization


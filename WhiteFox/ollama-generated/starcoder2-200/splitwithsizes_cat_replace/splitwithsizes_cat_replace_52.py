
class Model(torch.nn.Module):
    def __init__(self, split_sizes=None, dim=-1):
        super().__init__()
 
        self.split = torch.nn.Sequential(*[
            torch.nn.Conv2d(3, 8, k) for i in range(4)] + [torch.nn.Identity()])
 
        self.concat = torch.nn.Concat()
 
    def forward(self, x):
        # split_sizes: list of ints
        splitted_tensors = [
            self.split(x) for i in range(len(split_sizes))]
        return self.concat(*splitted_tensors)

# Initializing the model
split_sizes  = [32] * 4 + [16]
m  = Model(split_sizes=split_sizes, dim=-1)
x1  = torch.randn(1, 800, split_sizes[-1])
__output__  = m(x1)


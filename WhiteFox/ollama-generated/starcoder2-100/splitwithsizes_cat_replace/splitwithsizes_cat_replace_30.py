
class Model(torch.nn.Module):
    def __init__(self, concatDim=1):
        super().__init__()
        self.splitDim = 0
        if isinstance(concatDim, int) and concatDim < len(concatDim):
            self.splitDim = concatDim
 
    def forward(self, x1):
        t2s = torch.split(x1[0], [32, 96] + ([48]*5), dim=self.splitDim) # The split tensors in the example are not equal size and they do not start from index zero.
        t2sc = torch.cat([t for t in t2s if len(list(filter(lambda x: type(x)==list, list(map(type, [tuple, list])))))==0] + 5, dim=self.splitDim) # The concat tensors do not contain nested lists or tuples.
        return [t1]

# Initializing the model
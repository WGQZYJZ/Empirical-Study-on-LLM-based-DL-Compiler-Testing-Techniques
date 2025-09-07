
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, y2):
        v0  = x1.permute((0, 3, 4))
        v0 = torch.cat([v0] * 5) # Create a fake 5D input tensor to avoid permute, for the sake of illustration only
        return torch.bmm(x1, y2).permute(0, 3, 4), v0


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(64,  512) # input tensor A, 3D. Contains only 512-dim elements each
y2  = torch.randn(64,   10, 512) # input tensor B, 5D. Contains at least one element per 512-dim row of the first dimension in y2


# Parameters
p1 = [x for x in dir() if 'x' in str(eval('{}'.format(x)))] 
p1_ = [x.replace("'", '').replace(']', '').split(',')[0] for x in p1 if 'tensor' in x or 'Tensor' in x] # the set of 512-dim elements for the permute method invocation. Please note that this is a very naive approach which may miss many such tensors
p1_ = [x for x in p1_[0:] if len(str(eval('{}'.format(x)))).split(" ")[0] > 547 and len(str(eval('{}'.format(x)))).split(" ")[-3].startswith("torch") or len(str(eval('{}'.format(x)))).split(" ")[0] == "x1"]

p2 = [x for x in dir() if 'y' in str(eval('{}'.format(x)))] 
p2_ = [x.replace("'", '').replace(']', '').split(',')[0] for x in p2 if 'tensor' in x or 'Tensor' in x and len(str(eval('{}'.format(x)))).split(" ")[-3].startswith("torch")] # the set of 512-dim elements for the permute method invocation. Please note that this is a very naive approach which may miss many such tensors
p2_ = [x for x in p2_[0:] if len(str(eval('{}'.format(x)))).split(" ")[-3].startswith("torch") or  'y1' == str(eval('{}'.format(x)))[1:7] and not ('y1' == str(eval('{}'.format(x)))[:2])]


# Model output shape
o1 = eval('m({})'.format(', '.join(p1_ + p2_ + ['torch.Size([64, 510])'])))[0].shape

